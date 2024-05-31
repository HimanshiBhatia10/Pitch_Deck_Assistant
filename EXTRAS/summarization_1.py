import requests

url = "https://api.meaningcloud.com/summarization-1.0"

payload={
    'key': 'a228487ba7e0ca34d341e48d9f4fc06f',
    'txt': '''

ABOUT US
ABC_10 HEALTH CARE PRIVATE LIMITED is a dynamic and forward- thinking  company  in  the  dermatological  industry,  striving  to become a leading player in India. Our core mission is to offer high- quality dermatological products at affordable prices, with a focus on benefiting society. We source our products exclusively from GMP, WHO, and ISO-certified manufacturers and distribute them to healthcare  professionals  in  an  organized  manner.  With  a dedicated team and a commitment to excellence, we are poised to make a positive impact on the skincare landscape in India.
MISSION
Our company is committed to achieving a prominent position in
the dermatological industry in India.
VISION
We aspire to make a meaningful impact on society by providing high-quality products at affordable prices.

Problem Faced
Delayed Payments:
One prevalent issue in the industry is delayed payments, which can disrupt
cash   flow   and   affect   business
SOLUTIONS WE PROVIDE
Advanced Payment System
01  Encouraging advance payments to
reduce delayed payments.

Inventory Optimization

operations.
Excessive Product Offers:
The  market  is  often  saturated  with numerous product offerings, making it challenging  for  customers  to  make informed choices.
Implementing efficient inventory management to minimize overstock and waste.

Product Streamlining
Simplifying product offerings for easier customer decision-making.

PRODUCT PORTFOLIO





Skin lightening tablets                   Sunscreen                      Hair tablets





shampoos                              Lip balm

MARKET SIZE
The  skincare  products  market  was  valued  at  INR
129.76 Bn in 2020 and is expected to expand at a compound  annual  growth  rate  (CAGR)  of  ~8.22% during the 2021 - 2025 period, to reach a value of INR
191.09  Bn  by  2025.  Some  of  the  key  players  that
operate in the market are Hindustan Unilever Limited, The Himalaya Drug Company, Emami Limited, and Nivea India Private Limited.

TAM            SAM

INR 129.76
Bn
INR 68.76
Bn


Sources: Research and Markets

TARGET MARKET
Dermatologists:
Approximately 12,000 practicing dermatologists in India.
General Practitioners:
Over 100,000 general practitioners who occasionally prescribe dermatological products.
Pharmacists:
More than 200,000 pharmacists who stock and recommend skincare and dermatological products.
Cosmetic Clinics and Spas:
Over 10,000 cosmetic clinics and spas that use and retail skincare and dermatological items.





COMPETITORS

Dermaceutics
Galderma





Glenmark            Sebamed
COMPETITIVE ADVANTAGE
Quality Assurance
We have a strong commitment to sourcing products exclusively   from   GMP,   WHO,   and   ISO-certified manufacturers, ensuring the highest standards of quality and safety for our customers.
Focused Product Offerings
We stand out by streamlining our product portfolio to emphasize the most essential and effective products, reducing customer confusion and promoting the quality of our core offerings.
Advance Payment System
Our  innovative  approach  of  encouraging  advance payments  has  improved  our  cash  flow  and  financial stability, allowing us to invest in product development and customer service.

UNIQUE SELLING POINTS
Result-Oriented Products:
Our products are designed to deliver effective, long-lasting results, addressing your dermatological needs comprehensively.
Minimal Side Effects:
We prioritize safety by ensuring that our products have minimal side effects, minimizing any potential discomfort or risks.
Affordable Pricing:
Our commitment to affordability means that you can access top-quality dermatological solutions without breaking the bank.
Customer-Centric Approach:
We put your well-being first, tailoring our products and services to meet your unique needs and preferences.

REVENUE MODEL
The primary revenue stream for our company would be selling our range of creams, face washes, Hair Tablets, and pigmentation cream. We offer these products through various channels such as our own website and online markets.








Business To Business        Business To Customer          Wholesale & Retails

CUSTOMERS VALUE
Holistic  skincare  experience  that  nourishes  the body and soul.

Use of pure, all-natural ingredients derived from natural product wisdom.

Addressing different skin concerns and enhancing skincare routines.

Promotion of youthful, radiant, and ageless beauty.

Commitment to sustainability, ethics, and respect for the environment.

AIM TO SCALE UP
Market Expansion:
Identify and enter new geographic regions and markets within India to tap into a broader customer base.


E-commerce Integration:
Strengthen   our   online   presence   and   e-commerce capabilities  to  reach  a  wider  audience  and  facilitate convenient product purchases.

Distribution Network:
Establish  strategic  partnerships  and  collaborations  with pharmacies,  clinics,  and  hospitals  to  ensure  efficient product distribution and availability.

FUND UTILIZATION



NAME OF STARTUP:
ABC_10 HEALTH CARE PRIVATE LIMITED
Tools and equipment 22.5%



FUNDING SCHEME:              START UP INDIA SEED FUND SCHEME

FUNDING TYPE:                 SEED FUND GRANT

TOTAL FUND REQUIRED:           Rs. 20,00,000








Product Testing 17.5%
Developing Products 37.5%


Particulars           October             November      December      January         Total


Developing Products
4,00,000             3,50,000                                   7,50,000
Manpower 22.5%

Manpower           2,50,000             2,00,000                                  4,50,000


Product Testing
Tools
and equipment

Total per Milestone
2,00,000       1,50,000         3,50,000

2,50,000       2,00,000        4,50,000

6,50,000             5,50,000       4,50,000        3,50,000        20,00,000

MEET OUR CEO









Mr. J.LC
CEO and Director
J.  LC is  a  qualified individual  with  a  D  Pharm  degree and  possesses  an  impressive  21 years    of    experience    in    the pharmaceutical      and      derma cosmetic industry.

LET'S WORK TOGETHER
Email :
DIRECTOR@ABC_10.COM
Phone :
+91-90000000
Address :
ABC_10 
''',
    'sentences': '20'
}

response = requests.post(url, data=payload)

print('Status code:', response.status_code)
print(response.json()["status"])
result = response.json()["summary"]

f = open("/Users/thestash/PycharmProjects/Pitch_Deck_Analysis/t.txt", "w")
f.write(result)
f.close()