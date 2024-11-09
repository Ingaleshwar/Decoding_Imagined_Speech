# Abstract
Speech in both overt and covert forms are very natural to human beings. During covert speech, human imagine speaking without any intentional movement of any articulators. Brain cells show different electrical activities depending on people’s imagination. Electroencephalogram (EEG) is a noninvasive technique that records electrical activity in the
human brain of imagined speech. These signals can be used under a Brain-Computer Interface (BCI) framework, for possible decoding of imagined speech.
<br>
This project aims to build an assistive technology that provides a new communication channel for people who are unable to speak due to motor disabilities, such as Locked-inSyndrome in which they are not capable to communicate due to the complete loss ofmotor control. BCI systems using EEG are still facing several challenges that have to beaddressed in order to be applied to solve real life problems.
<br>
From an accessible source, the EEG signals corresponding to three words are collected. Subsequently, The signals undergo pre-processing, feature extraction, and a support vector classifier is built using training samples. The trained model is deployed on a Raspberry Pi. When tested using test samples the system is able to decode the imagined word correctly with an accuracy of 35%. The imagined word is displayed using LCD. A robotic arm is also built that performs a gesture of the imagines word.<br>
<b>Keywords: Electroencephalogram , Brain-Computer Interface , Assistive technologies, Raspberry Pi.</b>
<hr>
<h1>Objective of the project</h1><br>
The key objectives of the project are:<br>
1. To develop a classifier to classify three imagined words from EEG data.<br>
2. To deploy the model on Raspberry Pi .<br>
3. To design a robotic arm for gesturing the imagined word.<br>