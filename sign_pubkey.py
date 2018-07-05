>>> import pybtc
>>> a = pybtc.Address("cP6Yo1Dm2Gx96gRWyxZ3B6gECpP9cMeD5oxd7Xs1qtW5knG8AgPm", address_type="PUBKEY", testnet=True)
>>> a.address
'mjfWnmR8fRdmKKFBvkrRMAKNrthfzE6rNK'
>>> tx = pybtc.Transaction(testnet=True)
>>> tx.add_input("0b7527ede5de924f91dc02e29de99c1a5595c1ac13dcf9bf702ce33cf1c9ddaa")
>>> tx.add_output(128000000, address="n4AYuETorj4gYKendz2ndm9QhjUuruZnfk")
>>> tx.sign_input(0, private_key="cP6Yo1Dm2Gx96gRWyxZ3B6gECpP9cMeD5oxd7Xs1qtW5knG8AgPm", script_pub_key=a.pubkey_script)
>>> tx.serialize()
'0100000001aaddc9f13ce32c70bff9dc13acc195551a9ce99de202dc914f92dee5ed27750b000000004847304402207ee89eceb8e3999d2c5ba4d902de91c2418f4e4b94bb76b1f57efc2c6d4e814d02207b43e3c38a3c35a722999bd1eee53153445948691b695e2158e11ec5485bb80a01ffffffff010020a107000000001976a914f86f0bc0a2232970ccdf4569815db500f126836188ac00000000'
