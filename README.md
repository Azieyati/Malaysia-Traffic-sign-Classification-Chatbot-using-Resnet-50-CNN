# MALAYSIAN-ROAD-SIGN-RECOGNITION-CHATBOT-USING-Resnet-50-CNN

## ABSTRACT
Traffic signs are an important thing to provide information about what happens on the road while driving or walking. It also may cause an accident if the road user is not aware of traffic signs on the road. In another hand, tourists or international students who drive in Malaysia also may have the same problem and some of them maybe don’t understand the meaning of road signs in Malaysia. This project is to focus on detecting the traffic/road signs on the roadside using Convolution Neural Network with PyTorch. This is done by initially analyzing the requirements followed by designing the architecture, implementing, and testing the chatbot. In developing the chatbot, a CNN model is trained with pre-processed datasets to predict the recognition of the traffic/road signs. The recognition accuracy achieved higher than 90% recognition accuracies for traffic signs using Malaysia’s traffic sign data set. This system will help the driver to learn and get knowledge about the meaning of traffic signs. It seems like a simple problem but may have a significant impact on their lives and their environment if this problem is ignored. It is also easy to access the system because the user just needs to search for the "DRIEBIE" chatbot on Telegram and then can easily access and learn from there. Users don’t need to install additional software or hardware to get the system and it’s free for anyone who needs it. The system requires users to send an image of a traffic sign on the road as input, then the system will provide explanations, and instructions to help users to refer and make decisions.

## INTRODUCTION
Road signs are visual symbols or markings placed along roadways to provide information, guidance, and warnings to drivers, pedestrians, and other road users. They play an important role in ensuring safety and promoting efficient traffic flow. Road signs convey various types of information, such as regulatory instructions, warnings of potential hazards, guidance for directions, and important information about the road and its surroundings. It is important to familiarize yourself with the meaning of different road signs and their implications to avoid accidents. Moreover, road signs are like a language that the road wants to convey to drivers which gives relevant information on when to turn, street names, routes, directions, and warning for drivers. This road sign also helps drivers to keep them safe while driving. Without the knowledge of road signs, they hardly recognize what happens in front of them and tend to cause rising accidents in those areas. Some drivers might not realize this, but the road and safety signs in Malaysia have different meanings and functions according to their shape, font size, signboard color, placement, and symbol (Asyraf, 2022) The purpose of CHATDRIBIE which is known as the Malaysian road sign classification system in Chatbot aims to provide important information and instructions to the road users and to accurately classify traffic signs based on their visual content. This classification system enables the chatbot to provide users with relevant information, guidance, and assistance related to specific traffic signs. Furthermore, this system also focuses on helping road users who are still new in driving and doesn’t remember the meaning of road symbol it is also useful for tourist who drives in Malaysia so that they can better understand the meaning of the road signs. The chatbot will require users to send an image of road signs then it will explain in detail the meaning of the road signs and the instruction on what they should do.


## Objectives
This project embarks on the following objectives:
1. To identify the requirements for developing a road sign recognition chatbot.
2. To develop a road sign recognition chatbot for Malaysian road signs.
3. To test the performance of the chatbot using quantitative and qualitative methods.

## Target user:
- Newbie drivers
Newbie drivers refer to individuals who have recently obtained their 
driver's license or have limited driving experience. They may lack confidence and knowledge in various aspects of driving, including road rules, traffic signs, and 
 safe driving practices.
- Tourist who drives in Malaysia
This user group consists of tourists who are studying or just visiting Malaysia and choose to explore the country by driving. They may be unfamiliar with Malaysian roads, traffic regulations, and local driving customs.


## Project Significance
This project is focusing on helping the newbie driver to better understand the meaning of each traffic/road sign in a different way. It also potentially enhances road safety, improves driver awareness, and contributes to a more efficient and organized traffic system. In addition, the project also contributes to the education and awareness of drivers, particularly those who are less experienced or unfamiliar with certain traffic signs. The chatbot can provide explanations, and instructions to help users to refer and make decisions, empowering them to become safer and more informed drivers. As a result, by leveraging the power of computer vision and machine learning, the project addresses crucial aspects of traffic management, aiming to create safer, more informed, and more efficient systems.


## Use-case Diagram
![image](https://github.com/Azieyati/Malaysia-Traffic-sign-Classification-Chatbot-using-Resnet-50-CNN/assets/156404474/dbf3c261-596d-4205-9b30-e3bf0eb3df23)

## Confusion Matrix

![image](https://github.com/Azieyati/Malaysia-Traffic-sign-Classification-Chatbot-using-Resnet-50-CNN/assets/156404474/4454e4b9-d0db-4da6-bf48-9f8a8c7b5f52)


![image](https://github.com/Azieyati/Malaysia-Traffic-sign-Classification-Chatbot-using-Resnet-50-CNN/assets/156404474/a2f4466f-1daa-4a3b-833d-c04ba4d3836e)

#### Accuracy = correct_predictions / total_samples
#### Accuracy = 95/95*100 = 100%


## Comparison other CNN model
![image](https://github.com/Azieyati/Malaysia-Traffic-sign-Classification-Chatbot-using-Resnet-50-CNN/assets/156404474/bbb1fcae-195a-432f-8346-7e3f412d8f65)


## Comparison result using real-world image

![image](https://github.com/Azieyati/Malaysia-Traffic-sign-Classification-Chatbot-using-Resnet-50-CNN/assets/156404474/c6d3c6e8-9e52-49db-8bb1-fc473474d391)

## Conclusion
- The comparative analysis of three CNN models, Resnet-50, DenseNet, and VGG-16, when tested on real-world images characterized by differences in brightness, distance, and image quality, reveals that Resnet-50 emerges as the most suitable model for the project. 
- Meanwhile the comparison between public dataset and custom dataset show the custom dataset produce the best result than the public dataset.
- In summary, the DRIBIE chatbot, powered by the Resnet-50 deep learning model, has achieved an incredible 100% accuracy rate across near and far objects. This remarkable success demonstrates the accuracy and versatility of the model, laying the foundation for exciting future applications.


#### +----------------------------------------------------------------------+
#### | Objectives                    |   Conclusions                        |
#### +-------------------------------+--------------------------------------+
#### | To identify the requirements  | This project has successfully met the| 
#### | for developing a road sign    | objective of identifying all the     |
#### | recognition chatbot.          | specific requirements for developing | 
#### |                               | a road sign recognition chatbot.     |
#### +-------------------------------+--------------------------------------+
#### | To develop a road sign        | This project has successfully        | 
#### | recognition chatbot for       | achieved the second objective of     |
#### | Malaysia road signs.          | successfully developing a road sign  | 
#### |                               | road signs by exceeding our target   |
#### |                               | with an accuracy rate of over 90%.   |
#### +-------------------------------+--------------------------------------+
#### | To test the performance of    | This project have successfully       | 
#### | the chatbot using quantitative| accomplished our objective of        |
#### | and qualitative methods.      | assessing the chatbot's performance  | 
#### |                               | through a thorough evaluation that   |
#### |                               | combines quantitative and qualitative|
#### |                               | methods.                             |
#### +-------------------------------+--------------------------------------+


