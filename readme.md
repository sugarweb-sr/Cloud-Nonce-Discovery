 Cloud Nonce Discovery

-Created using Python 3
-pip install boto3
-pip install fabric
-install AWS
-AWS configure

-Python3 boto.py        
 create N instances and terminated all running instances in EC2
-fab cnd1:              
 upload work1.py and run it in the connecting instances
Or
-fab cnd2: parameter1(difficulty-level),parameter2(the number of VMs)  
upload the code to obtain a golden nonce with relevant difficulty-level