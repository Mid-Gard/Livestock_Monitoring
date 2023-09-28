**Case 1)**

Animals and Experiment Arena The study was carried out on a commercial dairy farm from 24 July to 1 August 2021 in Cao County, Heze City, Shandong Province, China. The research methods and use of animals in the experiments were approved by the Chinese Academy of Agricultural Sciences for experimental animal welfare and ethics (IAS2021-220). Fifty Holstein cows were housed in a free-stall barn with a length of 90 m and a width of 15 m. A total of 10 healthy lactating Holstein-Friesian cows were selected to attach in-house-designed IMU- based collars, and each cow was continuously monitored for at least seven hours during the experiments. The cows were milked at 8:30 am, 4:30 pm, and 12:00 pm every day. Seven cameras (Hikvison DS-2CE16G0T-IT3, Hikvison, Hangzhou, China) covered 90% of the barn area to record cattle behaviors, and video recording time and sensor time were synchronized. For the convenience of the observation, only day’s (08:30 a.m.–4:30 p.m.) data and videos were used for analysis in this paper.

**DEVICES:** The sensor device consists of a microprocessor, a Micro-Electro-Mechanical System (MEMS) IMU (MPU-6050, InvenSense, San Jose, CA, USA), a 4G transmission module, a GPS, and a wrapped battery (3.7 v, 1600 mAh) by a waterproof plastic box (Figure 1a). MPU6050 was chosen as the IMU in this work, which was composed of a 3-axis accelerom- eter (±4 g) and a 3-axis gyroscope (±2000 ◦/s). This low-cost IMU was widely used in wearable devices due to its low power consumption and high performance. The sampling frequency was set to 32 Hz (32 rows per second). To prevent the collision with the headlock, the sensor was fixed on the neck right behind the right ear (Figure 1b), and the weight below the neck was used to keep the sensor in place. The collected sensor data, sample time, device id, battery voltage, latitude, and longitude were encoded into hexadecimal and transmitted to the server using a 4G network every 40 s.

**CLASSES:**  
![[Capture.PNG]]

 **ML ALGORITHMS:**
 According to the stratified sampling method, 70% of each type of behavior was selected as the training set and the remaining 30% as the testing set. A 10-fold cross-validation method was adopted to obtain the parameters of each model. Three machine learning algorithms were used to classify cattle unitary behavior. The same dataset was applied to the three algorithms to fairly compare the classification performance.
  1. **K-nearest neighbors (KNN):** The rationale of the KNN algorithm is that each sample can be represented by the K nearest neighbors [27 ]. The classification for samples can be calculated by the distance between the testing sample and the training sample. This distance generally uses Euclidean distance or Manhattan distance. According to the order of distance, the testing sample is classified as the closest class to it. In order to measure the sample distance on the same scale, all features are normalized, and then the selection of K value is obtained through cross-validation. 
 2. **Random forest (RF):** The RF is a bagging ensemble algorithm [ 28]. RF trains a base classifier (cart decision tree) by randomly selecting some samples (with replacement) and extracting several fea- tures each time. The Gini coefficient is used to evaluate the effect of cart splitting, and all base learners vote to produce the final prediction. The weight of the base learner is the same, and thus the expectation of the model is approximately equal to that of a single base learner, and the variance is gradually reduced [29]. 
 3. **Extreme boosting algorithm (XGBoost):** The XGBoost is a boosting ensemble algorithm that efficiently implements the Gradient boosting decision tree algorithm [ 30 ]. The base learner is one kind of simple decision tree. The initial model is trained to fit the residual between the predicted value and the actual value of the model from the previous round. The penalty term is added to the loss function to prevent the model from overfitting.

**ACCURACY:**
![[Capture2.png]]

![[Capture3.PNG]]

**CONCLUSION:**
In this paper, a new framework was proposed for cattle behaviors classification via neck-worn IMU sensors in two steps: (1) unitary behaviors classification and (2) detailed movement analysis. This study showed that IMU sensors were not only able to distinguish unitary behaviors but also effectively identify non-constituent (feed tossing) and constituent movement (rolling biting and chewing) during unitary behaviors. All unitary behaviors were better recognized on the three algorithms (KNN, RF, and XGBoost) as the time window increased. The XGBoost algorithm had the best unitary behaviors classification performance under the 60 s time window with an average F1 score of 94%. The F1 score of feed tossing, rolling biting, and chewing were 78%, 87%, and 87%, respectively. It provided a new potential framework to monitor animal behavior and movement more comprehensively and improve farm management and animal welfare. Future research could be considered to demonstrate that more behaviors and detailed movements (e.g., tongue playing, excessive rub) could be recognized with this framework. Combining IMU time series and GPS location data will also provide insight into animal behavior in open pastures.

The behavior of livestock on farms is the primary representation of animal welfare, health conditions, and social interactions to determine whether they are healthy or not. The objective of this study was to propose a framework based on inertial measurement unit (IMU) data from 10 dairy cows to classify unitary behaviors such as feeding, standing, lying, ruminating-standing, ruminating-lying, and walking, and identify movements during unitary behaviors. Classification performance was investigated for three machine learning algorithms (K-nearest neighbors (KNN), random forest (RF), and extreme boosting algorithm (XGBoost)) in four time windows (5, 10, 30, and 60 s). Furthermore, feed tossing, rolling biting, and chewing in the correctly classified feeding segments were analyzed by the magnitude of the acceleration. The results revealed that the XGBoost had the highest performance in the 60 s time window with an average F1 score of 94% for the six unitary behavior classes. The F1 score of movements is 78% (feed tossing), 87% (rolling biting), and 87% (chewing). This framework offers a possibility to explore more detailed movements based on the unitary behavior classification.

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

**case 2):**

A total of 38 Holstein cows were used in this study. They were kept in free stall barns on four farms. Total mixed rations (TMR) were fed to the cows, and access to water and mineral blocks were ad libitum. No other feeds and supplements were given. Milking was conducted twice a day at a milking parlor on each farm. Herds scale, parities, and the days after calving are shown in Table 1. Although the record of the feed bank width per head was not made, it was judged that it exceeded the recommended value (> 46 cm) (Albright, 1993) from the visual observation. All the cattle used were healthy during this study.

**DEVICES AND DATA COLLECTION:** A logger-node (Bycen Co., Ltd, Kobe, Japan) was used to record ac- celeration. This logger-node was equipped with H30CD (Hitachi Metals, Ltd., Tokyo, Japan) as a three-axis accelerometer; its meas- urement range was ± 19.613 m/s2 and its precision was 12 bit. Acceleration data were stored in a built-in microSD card and used for analysis. The size of the logger-node was 58 ×42 × 16 mm (H×W×xD) and weighed 40.7 g. At the time of measurement, it was placed in- side a reinforced plastic case (measuring 4.2 ×9.0 × 14.0 cm, Pelican Products, Inc., Torrance, CA). The case was then attached to the col- lar of the cows (collars were approximately 120 cm wide × 4 cm high). with weight on ventral (600 g), adjusting the acceleration devices to always be placed on right side of each cow's neck (Figure 1). There was a space where the hand could easily be inserted between the collar and the skin. Data sampling frequency at the time of measure- ment was set as 20 Hz.

Changes in acceleration accompanying the movements of cows were recorded from 10:00 to 16:00 hr, for 6 straight hours. Simultaneously, cattle behavior was being visually observed every 1 min, and the be- haviors were classified as eating, rumination, standing, lying, walk- ing, drinking water, or other.

Visual inspection results of 10 cows in Farm A determined that the amount of time spent on eating/rumination/lying accounted for 94.8% of their total behavior (Table 3), so the analysis of the accel- eration data focused on these three behaviors. Table 4 shows the final epoch number used for the analysis of the acceleration data. No avoidance behavior and dysphagia were observed in the cows due to mounted logger-node.

**CLASSES:**
![[Capture4.PNG]]
![[Capture5.PNG]]

**ML ALGORITHM**S:

**simple decision tree:**
The advantage is that the decision tree method is easy to interpret by visualizing the classification process as a tree structure (Valletta et al., 2017). In addition, the CART algorithm (Breiman et al., 1984) is one of the most commonly used algorithms as a decision tree method, and it was also used in this research. It used “activity level” and “variations” as parameters, as those parameters could be obtained beforehand and because they presented clear differences between eating, rumination, and lying. As a result, this study had excellent precision (99.2% by cross- validation), and superb sensitivity and specificity (100% in the test data from other farms). Another report of behavior classification using three-axis accelerometers and decision trees, Diosdado et al. (2015) showed similar results: 98.78% sensitivity and 93.1% specificity for eating, and 77.42% sensitivity and 98.63% specific- ity for lying behavior. However, Diosdado et al. used VeDBA (an equivalent to activity level) and SCAY (a component of gravita- tional acceleration in y-axis) as parameters. This suggests that in the classification of eating and lying behaviors, the frequency of rapid change (i.e., “variations”) is more important than the gradient of the neck as a parameter added to the “activity level”. It was considered to be one factor that high classification accuracy was in this research. Therefore, the “variations” parameter may be an element that reflects the behavioral characteristics of cattle effi- ciently, and it was possible to clearly classify rumination behavior in fact. However, further investigation is necessary to clarify this reason. Anyway, it suggests the usefulness of activity level and variations as parameters of behavior classification.

**CONCLUSION:**

This study shows that collar-mounted three-axis accelerometers provide high precision data for calculating the activity level and vari- ations used in classifying the behaviors of dairy cows kept in free stall barns as eating, rumination, or lying. In addition, decision tree method is recommended as a behavior classification algorithm using these data. This method will be a useful tool for cattle herd manage- ment in the future.

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

**case 3):**

Autonomous sensor-based systems for monitoring cattle behavior have gained significant importance recently. These systems offer an improvement over traditional visual methods, which are both time-consuming and labor-intensive. One example of such a system involves neck-mounted collars that continuously monitor dairy and beef cattle. These collars automatically track and map key behaviors at the individual animal level, serving as a basis for decision support. This decision support helps inform interventions that enhance the efficiency of on-farm practices.

In this study, a novel approach to developing behavior classification algorithms is presented. This approach focuses on reducing the complexity of the data. Two feature selection techniques, based on Mutual Information (MI) scores and Backward Feature Elimination (BFE), are applied to time-series features extracted from raw accelerometer data. Initially, 42 features are extracted from the accelerometer signals, which are then reduced to 7 to optimize the discrimination between three primary cattle behaviors: 'eating,' 'rumination,' and 'other.'

The rationale behind selecting the combination of reduction techniques and classification algorithms is explained, and a systematic evaluation of performance is provided. The study explores the trade-off between model performance, computational complexity, and memory usage. The results indicate that the Backward Feature Elimination technique for feature selection provides features with high discriminatory power but comes at the cost of increased computational complexity.

After feature selection, Linear Discriminant Analysis is employed to create a classification model with an overall balanced accuracy of 0.83. This model is the most efficient among all the feature reduction and algorithm combinations considered for operational settings. It requires only 1.83 ± 1.00 ms for feature extraction and 0.05 ± 0.01 ms for inference, making it suitable for deployment within the computational and memory constraints of operational settings.

The study demonstrates that the proposed methodology is a viable option for advancing the use of low-cost neck-mounted accelerometer-equipped collars in precision livestock farming applications. The dataset generated during the study, including raw data and ground truth annotations from 18 steers, has been made publicly available to encourage the development of new models and facilitate comparisons between them (doi:10.5281/zenodo.4064802). Future research should aim to expand these trials with larger samples and longer observation periods to enhance the confidence in behavioral classification and identify additional value-added services.

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

**case 4)**


**Conclusion:**
In this study, data were meticulously gathered from a cohort of six dairy cows, and these animals were subjected to continuous monitoring over a substantial time frame spanning 36 hours. The primary objective of this data collection was to assess the performance of a decision-tree algorithm[6, 10, 22], k-means [11], SVM [8], and HMMs [23, 24]. in classifying various biologically significant behaviors exhibited by these cows. To ensure the accuracy and reliability of the algorithm's classifications, direct visual observations of each cow's activities were conducted and employed as a benchmark for validation.

**CLASSES:**
![[Capture6.PNG]]
![[Capture7.PNG]]

**RESULTS:**
The outcomes of this investigation are particularly noteworthy. The decision-tree algorithm demonstrated a remarkable ability to accurately categorize three distinct types of behaviors displayed by the cows. Firstly, it exhibited a sensitivity of 77.42% and a precision of 98.63% in identifying instances of the cows lying down. This means that the algorithm was adept at correctly identifying lying behavior in nearly 78% of cases, and when it classified a behavior as lying, it was correct almost 99% of the time.

Secondly, the algorithm displayed a sensitivity of 88.00% and a precision of 55.00% when it came to recognizing standing behavior. This implies that the algorithm effectively identified standing behavior in approximately 88% of instances, although it showed a relatively lower precision rate of 55%. This indicates that while it was good at detecting standing, it was sometimes prone to misclassifying other behaviors as standing.

Thirdly, the algorithm's performance in detecting feeding behavior was particularly impressive, with a sensitivity of 98.78% and a precision of 93.10%. This means that the algorithm excelled in identifying feeding activities in nearly 99% of cases, and when it labeled a behavior as feeding, it was accurate approximately 93% of the time. This high level of precision underscores the algorithm's capability to minimize false positives when categorizing feeding behavior.

Furthermore, the algorithm demonstrated its prowess in identifying transitions between standing and lying behaviors with an average sensitivity of 96.45% and an average precision of 87.50%. This signifies that the algorithm was exceptionally adept at recognizing shifts from standing to lying positions, correctly identifying these transitions in over 96% of cases, while maintaining a high level of precision at 87.50%. This is crucial as it reflects the algorithm's capability to pinpoint critical shifts in the cows' behavior accurately.

Notably, the remarkable sensitivity and precision exhibited by the decision-tree algorithm in this study are on par with, if not surpassing, the performance of more computationally demanding and resource-intensive algorithms such as hidden Markov models and support vector machines. This underscores the algorithm's efficiency and effectiveness, as it achieves comparable results without the computational overhead associated with these other methods.

In summary, the findings from this study highlight the exceptional capabilities of the decision-tree algorithm in accurately classifying and detecting various biologically relevant behaviors in dairy cows. These results not only validate the algorithm's effectiveness but also emphasize its potential as a practical and efficient tool for behavior monitoring in livestock management.

#############################################################################

**FLOW:**

1. **Data Collection:**
   - Attach 3-axis neck-mounted accelerometers to dairy cattle. These accelerometers can measure acceleration along three axes (X, Y, Z).
   - Record data over a specified time period, capturing the cattle's movements as they go about their daily activities.

2. **Data Preprocessing:**
   - Clean the accelerometer data to remove any noise or errors. This might involve filtering out spikes or erroneous readings.
   - Normalize or standardize the data to ensure that features are on a consistent scale.
   - Segment the data into time intervals (e.g., one-minute windows) to create a temporal context for analysis.
   - Extract relevant features from the data. These could include statistical measures (mean, variance), frequency domain features (e.g., Fourier transforms), and time domain features (e.g., duration of certain activities).

3. **Labeling:**
   - Annotate the data with ground truth labels for different cattle behaviors. Common behavior categories include grazing, resting, walking, eating, and other activities specific to dairy cattle.
   - This step involves manual observation and labeling by experts who can identify and categorize cattle behavior accurately.

4. **ML Models:**
1. **K-Nearest Neighbors (KNN)**:
   - K-Nearest Neighbors is a simple algorithm used for classification and regression tasks.
   - For classification, when you want to determine which category or class a new data point belongs to, KNN looks at the K nearest data points (neighbors) in the training dataset.
   - It calculates the majority class among those K neighbors and assigns it to the new data point.
   - For regression, KNN takes the average (or another aggregation) of the K nearest neighbors' values to predict a numerical outcome.

2. **Random Forest (RF)**:
   - Random Forest is an ensemble learning method that combines multiple decision trees to make predictions.
   - It creates a forest of decision trees, where each tree is trained on a random subset of the data and a random subset of the features.
   - When making a prediction, each tree in the forest votes, and the most popular prediction becomes the final output.
   - Random Forest is robust, reduces overfitting, and is used for both classification and regression tasks.

3. **XGBoost**:
   - XGBoost (Extreme Gradient Boosting) is a powerful gradient boosting algorithm used for supervised learning tasks.
   - It builds a strong predictive model by combining the predictions of many weak models (usually decision trees).
   - XGBoost uses a technique called gradient boosting, which iteratively improves the model's accuracy by focusing on the mistakes made in previous iterations.
   - It's known for its efficiency and effectiveness in various machine learning competitions and real-world applications.

4. **Simple Decision Trees**:
   - A decision tree is a tree-like model that makes decisions by following a path from the root (starting point) to a leaf (outcome).
   - At each internal node (decision point), a decision tree asks a yes/no question based on a feature of the data.
   - Depending on the answer, it follows the corresponding branch until it reaches a leaf node with a final decision or prediction.
   - Decision trees are interpretable and easy to visualize but can be prone to overfitting.

5. **Linear Discriminant Analysis (LDA)**:
   - Linear Discriminant Analysis is a dimensionality reduction and classification technique.
   - It aims to find a linear combination of features that best separates two or more classes in the data.
   - LDA looks for the projection direction (line or vector) that maximizes the ratio of the between-class variance to the within-class variance.
   - It's commonly used for tasks like face recognition and in situations where you want to reduce the dimensionality of the data while preserving class separability.

6. **K-Means**:
   - K-Means is an unsupervised clustering algorithm used to group similar data points together.
   - It starts by randomly selecting K cluster centers in the data space.
   - Data points are then assigned to the nearest cluster center based on a distance metric (usually Euclidean distance).
   - The cluster centers are updated iteratively by taking the mean of the data points in each cluster.
   - This process continues until convergence, and the result is K distinct clusters.

7. **Support Vector Machine (SVM)**:
   - SVM is a classification algorithm that finds a hyperplane (a line in 2D or a plane in higher dimensions) that best separates two classes.
   - It aims to maximize the margin, which is the distance between the hyperplane and the nearest data points from each class.
   - SVM can also handle non-linear separation by using kernel functions that map the data into higher-dimensional spaces.
   - It's effective in cases with high-dimensional data and is also used for regression and outlier detection.

8. **Hidden Markov Model (HMM)**:
   - Hidden Markov Models are used for sequential data analysis, such as speech recognition or natural language processing.
   - It models a system where you observe certain outcomes, but the underlying state of the system is hidden.
   - HMMs involve two main components: observable outcomes and hidden states, and they assume that the future state depends only on the current state (Markov property).
   - The model is trained to learn the probabilities of transitions between hidden states and the probabilities of observing specific outcomes from each state.

**Analysis of Above models for the project:**

1. **K-Nearest Neighbors (KNN)**:
   - Accuracy: KNN can perform well when there are clear clusters in your data, and neighboring data points of the same class tend to be similar. However, its accuracy can suffer when dealing with high-dimensional data or noisy data.
   - Performance: KNN's performance can be slow, especially with large datasets, as it requires calculating distances between data points for predictions.

2. **Random Forest (RF)**:
   - Accuracy: Random Forest is known for its high accuracy and robustness. It can handle both classification and regression tasks effectively. It's less prone to overfitting compared to individual decision trees.
   - Performance: RF can handle large datasets reasonably well, and its parallelization capabilities make it faster than single decision trees. It's considered a good choice for various applications.

3. **XGBoost**:
   - Accuracy: XGBoost is a state-of-the-art algorithm known for its high accuracy and competitive performance in machine learning competitions. It's suitable for both classification and regression tasks.
   - Performance: XGBoost is highly efficient and can handle large datasets and high-dimensional data. It's optimized for both speed and accuracy.

4. **Simple Decision Trees**:
   - Accuracy: Decision trees can work well for simple classification tasks but may suffer from overfitting for complex problems. Pruning and other techniques can help mitigate this.
   - Performance: Decision trees are fast and easy to interpret. They can handle large datasets reasonably well, but their performance might not be as high as ensemble methods like RF or XGBoost.

5. **Linear Discriminant Analysis (LDA)**:
   - Accuracy: LDA is effective when there are clear linear boundaries between classes. It's known for its simplicity and interpretability.
   - Performance: LDA is computationally efficient and can handle high-dimensional data. However, it may not perform well if classes are not well-separated linearly.

6. **K-Means**:
   - Accuracy: K-Means is a clustering algorithm, not a classification algorithm. It's used to group similar data points together, which may not be directly applicable to behavior classification.

7. **Support Vector Machine (SVM)**:
   - Accuracy: SVMs are effective when there's a clear margin of separation between classes, making them suitable for binary classification tasks. They can handle high-dimensional data effectively.
   - Performance: SVMs can be efficient, but their performance depends on the choice of the kernel and the size of the dataset.

8. **Hidden Markov Model (HMM)**:
   - Accuracy: HMMs are well-suited for sequential data like time series. They can be effective for behavior classification if your data exhibits sequential patterns.
   - Performance: HMMs can be computationally intensive, especially if the sequence data is long or complex.

For dairy cattle behavior classification using accelerometers, a good starting point could be Random Forest (RF) or XGBoost due to their high accuracy and versatility. However, it's essential to preprocess your data, choose appropriate features, and fine-tune hyperparameters to achieve the best results. Additionally, consider the interpretability of the model if it's crucial for your project. You may also want to explore the sequential nature of your data and see if Hidden Markov Models (HMMs) could be useful for capturing behavioral patterns over time.

6. **Model Training:**
   - Split the dataset into two parts: a training dataset and a testing dataset (e.g., 70% for training and 30% for testing).
   - Train model on the training data, using a criterion such as information gain or Gini impurity to determine feature splits.
   - The model will continue splitting nodes until a stopping criterion is met, such as a maximum depth or a minimum number of samples per leaf node.
   - Hyperparameters may need to be tuned to find the best tree structure.

7. **Model Evaluation:**
   - Assess the model's performance using various metrics, including:
     - Accuracy: The percentage of correctly classified instances.
     - Precision: The ratio of true positive predictions to the total predicted positives.
     - Recall: The ratio of true positive predictions to the total actual positives.
     - F1-score: The harmonic mean of precision and recall.
   - Evaluate the model on the testing dataset to ensure it generalizes well to new, unseen data.
   - Fine-tune the model as needed to improve its performance.

8. **Behavior Classification:**
   - Deploy the trained decision tree model to classify real-time accelerometer data from cattle.
   - As accelerometer data streams in, the model predicts the behavior of the cattle based on their neck-mounted accelerometer readings.

9. **Monitoring and Application:**
   - Continuously monitor cattle behavior in real-time using the deployed model.
   - Utilize the behavior classifications for various applications, such as optimizing feeding schedules, early detection of health issues, and overall herd management.
