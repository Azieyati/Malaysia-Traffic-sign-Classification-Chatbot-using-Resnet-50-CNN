import logging
import os

import torch
import telebot
from PIL import Image
from torchvision import transforms
from torchvision.models import resnet50, densenet121, vgg16

# Create the Telegram bot
bot = telebot.TeleBot('6135118251:AAETo4ZYabDbNDeUESmCEdvQO7FwzjAcATE')
num_classes = 9

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

# Initialize the model with pre-trained weights
# model = resnet50(weights=None)
# model.fc = torch.nn.Linear(2048, num_classes)  # Replace num_classes with the number of classes in your task
model = resnet50(weights=None)
model.fc = torch.nn.Linear(model.fc.in_features, num_classes)
# number of classes in your task

# original code
# model.fc = torch.nn.Sequential(
#     torch.nn.Linear(model.fc.in_features, 512),  # Adding a fully connected layer
#     torch.nn.ReLU(),
#     torch.nn.Dropout(p=0.5),  # Apply dropout with a dropout rate of 0.5
#     torch.nn.Linear(512, num_classes)  # Output layer for your specific classification task
# )

model.load_state_dict(
    torch.load('C:/Users/USER/PycharmProjects/projectPSM1/pretrained_model.pth', map_location=torch.device('cpu')))
model.eval()

# Define the device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# Define the label mapping
label_mapping = {
    0: 'Diverge',
    1: 'Give way',
    2: 'Height 5 Meters',
    3: 'Hump',
    4: 'No stopping',
    5: 'Obstruction',
    6: 'Speed Limit 80',
    7: 'Traffic Light',
    8: 'U-turn',

    # Add more label mappings as per your specific problem
}

# Define the image preprocessing steps
transform = transforms.Compose([
    transforms.Resize(224),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(degrees=(-15,15)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])


@bot.message_handler(commands=['start'])
def starting(message):
    bot.reply_to(message, "Hello, what can i help you ?")
    bot.send_message(
        message.chat.id, "Please choose one :\n"
                         "/Signboard - Road Sign information\n"
                         "/help - Show the instructions")


# Reply to
@bot.message_handler(commands=['Signboard'])
def greet(message):
    bot.reply_to(message, "Please noted that picture must be cropped following the traffic sign corner size")
    bot.reply_to(message, "Please send a photo of traffic signs...")


# Just send a message to reply
@bot.message_handler(commands=['help'])
def hello(message):
    bot.send_message(
        message.chat.id,
        "To identify a road sign, please follow these steps:\n\n"
        "1) Capture a clear image of the road sign you want to identify.\n\n"
        "2) Crop the image to focus specifically on the road sign, making sure to include the entire sign "
        "within the cropped area.\n\n"
        "3) Click the \"Send\" button to upload and submit your photo for analysis.\n\n\n"
        "By following these steps, you can provide me with the necessary information to assist you in identifying the "
        "type of road sign or provide any relevant information you may need about it.\n"
        "Feel free to proceed with the steps, and I'll be ready to assist you further!"

    )


@bot.message_handler()
def errormessage(message):
    if message.text.lower() == 'hello' or message.text == 'hey':
        bot.send_message(message.chat.id, "Hello, have a good day. Please send a photo")
    elif message.text.lower() == 'hi' or message.text == 'hai':
        bot.send_message(message.chat.id, "Hi !, have a good day. Please send a photo")
    elif message.text.lower() == 'bye' or message.text == 'goodbye' or message.text == 'good bye':
        bot.send_message(message.chat.id, "Bye, Thank you! Please visit again")
    elif message.text.lower() == 'help' or message.text == 'helps':
        bot.send_message(message.chat.id, "My only purpose is to tell you what kind of road sign it is. Send a photo")
    else:
        bot.send_message(message.chat.id, 'I do not understand what you wrote...')


# Handle all other messages.
@bot.message_handler(func=lambda message: True, content_types=['audio', 'voice', 'video', 'document',
                                                               'location', 'contact', 'sticker', ])
def default_command(message):
    bot.reply_to(message, 'This chatbot only accept image, please send a picture')


# Handle the "/classify" command
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.reply_to(message, 'picture is scan...')

    # Download the image sent by the user
    image_info = bot.get_file(message.photo[-1].file_id)
    image_file = bot.download_file(image_info.file_path)

    # Check the file type
    if image_info.file_path.endswith('.heic'):
        bot.reply_to(message, "Sorry, HEIC files are not supported.")
        return

    # Save the image locally
    image_path = 'user_image.jpg'
    with open(image_path, 'wb') as file:
        file.write(image_file)

    # Preprocess the image
    input_image = Image.open(image_path)
    input_tensor = transform(input_image).unsqueeze(0)

    # Perform inference using your PyTorch model
    with torch.no_grad():
        outputs = model(input_tensor)
        _, predicted_idx = torch.max(outputs, 1)
        predicted_label_idx = predicted_idx.item()

    # Map the predicted index to label text
    predicted_label = label_mapping.get(predicted_label_idx, 'Unknown')

    # Send the predicted label back to the user
    bot.reply_to(message, f"Traffic sign : {predicted_label} sign.")

    # Condition check
    if predicted_label_idx == 0:
        bot.reply_to(message, f"This sign is typically placed on overhead gantries or road signs ahead of a junction "
                              f"or interchange where traffic lanes split into separate directions."
                              f" It serves as an advance warning to drivers")
        bot.send_message(message.chat.id, f"Follow this instructions : \n"
                                          f"1) You need to choose the appropriate lane to follow their desired route\n"
                                          f"2) Avoid last-minute lane changes or confusion.")
    elif predicted_label_idx == 1:
        bot.reply_to(message, f"This sign is a downward-pointing triangle with a red border and white background. ")
        bot.send_message(message.chat.id, f"Follow this instructions :\n"
                                          f"1) Indicates that drivers approaching the sign must yield to other vehicles"
                                          f"on the intersecting road.")
    elif predicted_label_idx == 2:
        bot.reply_to(message, f"The Height 5 Meters sign is typically placed near low clearance areas, such as "
                              f"bridges, tunnels, or underpasses, where the vertical clearance is limited to 5 "
                              f"meters. The purpose of this sign is to alert drivers of vehicles that exceed this "
                              f"height restriction, ensuring they are aware of the potential hazard and can take "
                              f"appropriate measures to avoid entering the area.")
        bot.send_message(message.chat.id, f"Follow this instruction:\n"
                                          f"1) Only vehicle has the higher not exceed than 5 meters can entering "
                                          f"the area")
    elif predicted_label_idx == 3:
        bot.reply_to(message, f"The Hump Sign serves as a warning to drivers to slow down and be prepared to encounter "
                              f"a raised section of the road designed to slow down vehicle speed. Road humps are "
                              f"typically installed in areas where traffic calming measures are implemented "
                              f"such as residential areas, school zones, or areas with high pedestrian "
                              f"activity.")
        bot.send_message(message.chat.id, "Follow this instruction :\n"
                                          "1) Reduce your speed to safely navigate the road hump \n"
                                          "note: Speeding your car may cause damage to your vehicle")
    elif predicted_label_idx == 4:
        bot.reply_to(message, f"This sign is a red circle with a white border and a black symbol of a stopped "
                              f"vehicle. It indicates that stopping is prohibited in the designated area, even for a "
                              f"short duration.")
        bot.send_message(message.chat.id, "Follow this instruction:\n"
                                          "1) When you found this sign board, you are not allowed to stop your car"
                                          "even in the short time")
    elif predicted_label_idx == 5:
        bot.reply_to(message, f"The Obstruction Sign in Malaysia is a rectangular sign with a white background and a "
                              f"red border. It features a black symbol of an object obstructing the road, such as "
                              f"a fallen tree or a large rock. This sign indicates the presence of an obstruction on"
                              f"  the road ahead.")
        bot.reply_to(message, "Warning :\n"
                              "Be careful, obstruction on the road ahead")
    elif predicted_label_idx == 6:
        bot.reply_to(message, f"The Speed Limit 80 Sign in Malaysia is a circular sign with a white background and a "
                              f"red border. It features the number \"80\" in black, indicating the maximum speed "
                              "limit in kilometers per hour (km/h) for "
                              "that particular section of the road.")
        bot.reply_to(message, f"Instruction:\n"
                              f"The Speed Limit 80 Sign signifies that the maximum permitted speed for vehicles in "
                              f"that area is 80 km/h.")
    elif predicted_label_idx == 7:
        bot.reply_to(message, f"This sign is a white rectangle with a black border and the symbol of a traffic light. "
                              f"It indicates that a traffic light-controlled intersection is ahead.")
        bot.send_message(message.chat.id, "Instruction:\n"
                                          "1) Slow down your car\n"
                                          "2) Stop when the traffic light is RED color, and move when its GREEN")
    elif predicted_label_idx == 8:
        bot.reply_to(message, f"The U-turn Sign indicates the location or direction where drivers are allowed to make "
                              f"a U-turn on the road. A U-turn is a maneuver where a vehicle turns around to travel "
                              f"in the opposite direction. This sign is typically placed at intersections or specific "
                              f"locations where U-turns are permitted.")
        bot.send_message(message.chat.id, "Instruction:\n"
                                          "1) Take a lane from the far left lane on your side\n"
                                          "2) Give a left turn signal. Then, stop and check for oncoming traffic,"
                                          "vehicle\n"
                                          "3) Complete the U-turn in the right lane traveling in the opposite "
                                          "direction\n")

    # Delete the local image file
    os.remove(image_path)


# Start the bot
bot.polling()
