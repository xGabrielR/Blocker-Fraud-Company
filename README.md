# Blocker Fraud Company

![fraud_logo](https://user-images.githubusercontent.com/75986085/169668681-e233cf36-14da-4cf7-bfb3-e98010758a01.png)

<h2>Summary</h2>
<hr>

- [0. Bussiness Problem](#0-bussiness-problem)
  - [0.1. What is a Service](#01-what-is-a-service)
  - [0.2. What is a Fraud](#02-what-is-a-fraud)
  - [0.3. Fraud in Financial Transactions](#03-fraud-in-financial-transactions)
    - [0.3.1. Types of Transactions](#031-types-of-transactions)
      - [0.3.1.1. Cash Transactions](#0311-cash-transactions)
      - [0.3.1.2. Transfer](#0312-transfer)
      - [0.3.1.3. Debit](#0313-debit)
      - [0.3.1.4. Payment](#0314-payment)
- [1. Solution Strategy and Assumptions Resume](#1-solution-strategy-and-assumptions-resume)
  - [1.1. First CRISP Cycle](#11-first-crisp-cycle)
- [2. Exploratory Data Analysis](#2-exploratory-data-analysis)
  - [2.2. Top 3 Eda Insights](#22-top-3-eda-insights)
- [3. Data Preparation](#3-data-preparation)
  - [3.1. Encoding and Rescaling](#31-encoding-and-rescaling)
  - [3.2. Feature Selection](#32-feature-selection)
  - [5.3. Model Metrics](#53-model-metrics)
- [4. Embedding Space Study](#4-embedding-space-study)
- [5. Machine Learning Models](#5-machine-learning-models)
- [6. Model Tuning](#6-model-tuning)
- [7. Model Bussiness Results](#7-model-bussiness-results)
- [9. References](#9-references)

---

<h2>0. Bussiness Problem</h2>
<hr>

<p style="text-align:center;"><i>"Blocker Fraude Company is a company specialized in fraud detection in financial transactions made through mobile devices. The company has a service called “Blocker Fraud” with guarantee of blocking fraudulent transactions."</i></p>

<p>The company's business model is of the service type with monetization made by the provider's performance, that is, the user pays a fixed fee on the success in the detection of service fraud of the customer's transactions.</p>

<p>You have been hired by a DS consultancy to create a highly accurate and accurate model for fraud detection of transactions through mobile devices. You need to deliver an API with access to the model and also the answers to the following questions:</p>

> *1. What is the precision and accuracy of the model?*
> 
> *2. How reliable is the model in classifying new transactions?*
> 
> *3. What is the company's expected revenue if 100% of the transactions are classified with the model?*
> 
> *4. What is the price expected by the company if the model fails?*
> 
> *5. What is the expected profit for using this model?*

<h3>0.1. What is a Service</h3>

<p>Service is a business model like consultory, the company make a work and receive a profit based on her work results. For example, the Blocker Fraud Company, In Brazil, the company start with a new method of services to get some new clients based only on your "Blocker Fraud" model.</p>
<p>At Blocker Fraud it is B2B, Business to Business, Blocker Fraud offers the service to other businesses like banks and finance houses</p>

> *1. The company will receive **25%** of the value of each transaction that is **truly detected as fraud**.*
> 
> *2. The company will receive **5%** of the value of each transaction **detected as fraud, however the transaction is truly legitimate**.*
> 
> *3. The company will refund **100%** of the value to the customer, for each transaction **detected as legitimate, however the transaction is truly a fraud**.*

<p>For the customer it is an excellent deal, although the fee charged for the service is very high above 25% of success, the company will reduce its costs with fraudulent transactions detected as true frauds, but it will have a loss caused by the error in the service that will be covered by the own company.</p>
<p>In addition to attracting new clients from Brazil, with this risky strategy of guaranteeing reimbursement in case of failure, it specifically depends on the precision and accuracy of the model in carrying out these detections.</p>

<p>B2B Metrics is very important, let's check some ones!</p>
<ul>
  <li>💸 Market Strategy;</li>
  <li>💸 Target Clients;</li>
  <li>💸 Number of New Clients;</li>
  <li>💸 Client Aquisition Cost;</li>
  <li>💸 Lead Conversion Rate;</li>
  <li>💸 Churn Rate;</li>
</ul>

<h3>0.2. What is a Fraud</h3>

<p><i>"Wrongful or criminal deception intended to result in financial or personal gain."</i>~ Wiki</p>

<p>Fraud is an intentionally deceptive action designed to provide the perpetrator with an unlawful gain or to deny a right to a victim. In addition, it is a deliberate act (or failure to act) with the intention of obtaining an unauthorized benefit, either for oneself or for the institution, by using deception or false suggestions or suppression of truth or other unethical means, which are believed and relied upon by others. Depriving another person or the institution of a benefit to which he/she/it is entitled by using any of the means described above also constitutes fraud.</p>

<p>Types of fraud include tax fraud, credit card fraud, wire fraud, securities fraud, and bankruptcy fraud. Fraudulent activity can be carried out by one individual, multiple individuals or a business firm as a whole.</p>

<p>More Examples of Fraud:</p>

1. Data theft on fake websites.
2. Purchase of physical facilities.
3. Document change.
4. Computer data theft.
5. Interception of goods.
6. Phishing.
7. Bots and Stealing Files.
8. Receipts of or benefits not granted.
9. Ethics Violations.
10. Conflict of interests.
11. Appropriation or misuse of resources eg Supplies.

<p>Fraud involves the false representation of facts, whether by intentionally withholding important information or providing false statements to another party for the specific purpose of gaining something that may not have been provided without the deception.</p>


<h3>0.3. Fraud in Financial Transactions</h3>

<p>A financial transaction is an agreement, or communication, between a buyer and seller to exchange goods, services, or assets for payment. Any transaction involves a change in the status of the finances of two or more businesses or individuals. A financial transaction always involves one or more financial asset, most commonly money or another valuable item such as gold or silver.</p>


<h4>0.3.1. Types of Transactions</h4>

<h5>0.3.1.1. Cash Transactions</h5>

<p>A cash transaction is any transaction where money is exchanged for a good, service, or other commodity. Cash transactions can refer to items bought with physical money, such as coins or cash, or with a debit card. These differ from credit transactions because the money is immediately taken from the buyer and given to the seller.</p>
<p>A cash transaction stands in contrast to other modes of payment, such as credit transactions in a business involving bills receivable. Similarly, a cash transaction is also different from credit card transactions.</p>

<h5>0.3.1.2. Transfer</h5>
<p>A transfer is the movement of assets, funds, or ownership rights from one place to another. Is also used to describe the process by which ownership of funds or assets are reassigned to a new owner. Banking, brokerage, cryptocurrency, asset titles, and loan transfers are a few examples of domains and transaction types where transfers occur.</p>

<h5>0.3.1.3. Debit</h5>
<p>A debit card payment is the same as an immediate payment of cash as the amount gets instantly debited from your bank account.</p>
<p>Debit cards allow bank customers to spend money by drawing on existing funds they have already deposited at the bank, such as from a checking account. A debit transaction using your PIN (personal identification number), is an online transaction completed in real time. When you complete a debit transaction, you authorize the purchase with your PIN and the merchant communicates immediately with your bank or credit union, causing the funds to be transferred in real time.</p>
<p>In a credit card payment made by you, the amount is not debited from your bank account instantly. However, you are able to buy the product within your credit limit under the credit card. You need to make payment only after the generation of your credit card bill</p>

<h5>0.3.1.4. Payment</h5>
<p>An act initiated by the payer or payee, or on behalf of the payer, of placing, transferring or withdrawing funds, irrespective of any underlying obligations between the payer and payee.</p>
 
<h2>1. Solution Strategy and Assumptions Resume</h2>
<hr>

<p>The first problem finded is the massive size of dataset. The Dataset Info you can check below.</p>

<table>
  <tr>
    <td>Columns</td>
    <td>Rows</td>
  </tr>
  <tr>
    <td>11</td>
    <td>6353307</td>
  </tr>
</table>


<h3>1.1. First CRISP Cycle</h3>

<ul>
  <dl>
    <dt>Data Cleaning & Descriptive Statistical.</dt>
      <dd>The first step in data science projects is clean the dataset and check rows datatypes and fix simple wrong inputs. After dataset clean, the step is check with simple statistics methods the dataset behavior with (mean, median, std, skew, skew, kurtosis).</dd>
    <p>In this step I get some insight's and inconsistencies, you can check in this image below. 0 Transaction and 0 Median to newbalance_orig, the perpetrator clean the account.</p>
    <table>
      <tr>
        <td>newbalance_orig <b>Median</b></td>
        <td>Amount <b>Min</b></td>
      </tr>
      <tr>
        <td>0.0</td>
        <td>0.0</td>
      </tr>
    </table>
    <dt>Feature Engineering.</dt>
      <dd>In this step, with coggle.it to make a mind map and use the mind map to create some hypothesis list, after this list, I have created some new features based on differencies, like origin and destination balance diff, merchant flag and day based on "step" feature.</dd>
    <dt>Data Filtering.</dt>
      <dd>In first cycle I only selected a range of values to amount because in "big" transactions, in the dataset do not exists fraud on high values of transaction.</dd>
    <dt>Exploratory Data Analysis.</dt>
      <dd>In this step I deep dive in the dataset to shear for behaviors in three steps, the Univariable, Bivariable and Multivariable analysis to detect Fraud comportements, validation of bussiness hypothesis and correlations.</dd>
  </dl>
</ul>

<h2>2. Exploratory Data Analysis</h2>
<hr>

<h3>2.1. EDA On First Cycle</h3>

<p>I divide the EDA into three steps, univariable, bivariable and multivariable steps, In the univariable I check the target and all the characteristics (categorical and numerical), In the Bivariable, this step I validate 8 Business Hypotheses and in the Multivariable it is the correlations and the pair diagrams</p>

<p>Principal Results</p>

1. Usually after fraudulent transactions, all money is withdrawn from the destination account.
2. Only Transactions and Debit types have fraudulent activities.
3. The dataset does not follow a standard cash flow due to the simulator that generated the data.
4. There is not much information related to CASH-OUT to answer item 3, it can be assumed that the chash-out is a transaction worth 0 and therefore has some value that does not follow a flow.
5. the numerical variables have a distribution that can be seen by applying the log.
6. There is a spike in fraudulent transactions at the beginning of the simulation month.
7. Fraudulent transactions do not have negative diff in origin based on amount.
8. The larger the transaction, the more susceptible it is to fraud.

<h3>2.2. Top 3 Eda Insights</h3>
<hr>

<p>1. Debit transactions represent more than 50% of fraud cases.</p>

![fraud_per_day](https://user-images.githubusercontent.com/75986085/170603071-3aa00dd7-4532-417d-bc74-d831784703c4.png)

<p>2. Transactions after the 20th of the month account for 20% more fraud cases.</p>

![after_20_days](https://user-images.githubusercontent.com/75986085/170603088-84691292-e097-4d73-a224-5b3a7ea39ee9.png)

<p>3. 80% of fraud cases happen when the destination of the transaction already has money in the account.</p>

![fraud_amount](https://user-images.githubusercontent.com/75986085/170603081-50437ceb-03e6-4b01-a2a8-8f107a08215a.png)


<h2>3. Data Preparation</h2>
<hr>

<h3>3.1. Encoding and Rescaling</h3>
<p>In first cycle I only used Frequency Encoding for all categorical features and most robust scaler for numerical features because have extrema skewness on all numerical variables. But in EDA i see some good features to use log transformation too, for example the Amout have a cool normal shape when this feature is rescaled. For day feature I chose sin cos transformation.</p>

<p>In Second cycle I will go try log transformation and others encoding like One-Hot for type of payment because do not have any order on the transaction type, and I think the frequency encoding it's applying a bias on the transaction type because have different sizes of types in the same feature.</p>

![sizes](https://user-images.githubusercontent.com/75986085/172069361-76d5b73d-44b5-4d19-afc9-87ca6badf3da.png)

<p>But in EDA I have checked, only exists transaction fraud only on Debit and Transaction types in this feature.</p>

<h3>3.2. Feature Selection</h3>

<p>In first cycle I choose a simple and fast method to check feature importance using only two models, the Random Forest and XGBoost, in second cycle I will try Boruta.</p>

<p>In resume, the XGBoost have better results than Random Forest, But why XGB, he took the difference in type feature (cashin, cashout...) and didn't overfit the other features, the RF only selected two features.</p>



<h2>4. Embedding Space Study</h2>
<hr>

<p>Next Cycle</p>

<h2>5. Machine Learning Models</h2>
<hr>

<p>In this step to chose only used four models, the Stochastic Gradient Descent, LGBM, Random Forest Classifier and XGBoost Classifier for prediction with dataset splited in three, train, validation and test.</p>

<h3>5.1. Stochastic Gradient Descent</h3>
<p>The SGD is my second baseline model, in some cases this model fit's good the dataset and have good performaces, but for this dataset based on results of data preparation, the SGD do not haved a good performace than RF and XGB.</p>

<h3>5.2. XGBoost</h3>
<p>Better results of all models with all train dataset. With test dataset the results is:</p>

![xgboost](https://user-images.githubusercontent.com/75986085/172069967-41262d00-aba2-4be5-bb4f-d4472dc08d84.png)

<p>In cross validation with test dataset I get this results in both datasets:</p>

![cross](https://user-images.githubusercontent.com/75986085/172069901-ce050134-8145-4079-9fbf-dafc26ed1b7d.png)

<h3>5.3. Model Metrics</h3>

<p>The key of this results is the <b>Recall</b> of the model, Recall is a model performace metric based on "false negative". In Blocker Fraud with lower recall, the model is missing fraudulent transactions, this is horrible for the current business model which is based on whether or not to detect fraud, if the model misses a legitimate fraud it can cause a lot of financial damage especially if it is a very high transaction.</p>

<p>In the Confusion Matrix (2x2 cube plot) the model is missing <b>six</b> fraudulent transactions, and the question that remains, what if just one of these transactions cost the entire company? The bussiness model is, 100% of cash back if model miss the fraud!!</p>


<h2>6. Model Tuning</h2>
<hr>

<p>In this step, I have used this techniques:</p>
 
1. **Cross Validation**: To get the real performace of Model in some pices of dataset.

<p>Cross Validation for Default Model.</p>

![cross](https://user-images.githubusercontent.com/75986085/172069901-ce050134-8145-4079-9fbf-dafc26ed1b7d.png)

2. **Grid Search**: To maximize model performace based on model's parameters.

<p>Using Grid Search I get a more simple model with 85 estimators for example.</p>

3. **Change Threshold**: Analyze whether or not it is worth changing the Threshold for better performance.

<p>By Default, the sklearn define a threshold is .5, in this analysis I check what is the best threshold for this model to classify.</p>

![model_threshold](https://user-images.githubusercontent.com/75986085/172070281-157d3ee9-d034-4155-a402-6760a2c8fce9.png)

4. **Calibration Curves**: Calibrate the model for better performace.

<p>Predicted probabilities that match the expected distribution of probabilities for each class are referred to as calibrated. The distribution of the probabilities can be adjusted to better match the expected distribution observed in the data.</p>

<h2>7. Model Bussiness Results</h2>
<hr>

<p>Now, based on bussiness I will translate model performace on bussiness performace. In other words, how much money will I make using the model?</p>

<h4>1. What is the precision and accuracy of the model?</h4>

<p>The precision and the accuracy of model results in One training and testing is 0.999994 for accuracy and 0.99513 for Precision. But this two metrics is do not good for Blocker Fraud, because if model wrong the fraud detection, he needs to refund 100% of transaction amount, because this i used recall two.</p>

<p>If lower Recal much chance to have False Negative (Fraud but model classify with No Fraud). For recall in one training and testing I get 1.0 recall based on amount of no fraud detected.</p>

<p>In cross validation i get 0.9951 + / - 0.0 of Recall.</p>


<h4>2. How reliable is the model in classifying new transactions?</h4>

1. Answer in Second Cycle!


<h4>3. What is the company's expected revenue if 100% of the transactions are classified with the model?</h4>

1. If all **trully transactions detected as a fraud**, the company will **receive** a total of **R$ 56616833024,00**.
2. If all **fraudulent transactions is detected** by model, the company will **receive** a total of **R$ 3014103808,00**.
3. Total **money obtained by only correct detections** is **R$ 59630936064,00**.

<h4>4. What is the price expected by the company if the model fails?</h4>

1. If all fraudulent transactions in dataset is **not detected**, the company will **lost** **R$ 3014103808,00.**
2. The diference of detection is **R$ -9042311168,00**, if model miss, the company will have more loss.

<h4>5. What is the expected profit for using this model?</h4>

1. The company will **save a total** of **R$ +/- 11996415433,55** ONLY for fraudulent transactions on dataset!!

<p>The model miss six fraudulent transactions, to answer this I only sort values and drop the last six transactions with more amount.</p>

<h2>8. Model Deployment</h2>
<hr>

<p>Under Working.</p>


<h2>9. References</h2>
<hr>

<ul>
  <li><a href="https://www.serasa.com.br/ensina/seu-cpf-protegido/o-que-e-fraude/">Oque é Fraude?</a></li>
  <li><a href="https://blogbr.clear.sale/fraude-no-e-commerce-entenda-este-fen-meno-e-saiba-quais-s-o-os-principais-tipos">Fraude: Entenda oque é</a></li>
  <li><a href="https://distrito.me/blog/mobile-payment-o-que-e-como-funciona-e-tendencias-no-brasil">Tendências de Mobile Payment</a></li>
  <li><a href="https://www.investopedia.com/terms/f/fraud.asp">Fraud: What You Need to Know</a></li>
  <li><a href="https://cleartax.in/g/terms/cash-transaction">Cash Transaction</a></li>
  <li><a href="https://www.investopedia.com/terms/d/debit.asp">Debit</a></li>
  <li><a href="https://www.investopedia.com/terms/t/transfer.asp">Transfer</a></li>
  <li><a href="https://intellias.com/how-to-use-machine-learning-in-fraud-detection/">ML On Fraud Detection</a></li>
</ul>
