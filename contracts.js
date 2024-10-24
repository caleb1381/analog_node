const { waitReady } = require('@polkadot/wasm-crypto');
const { Keyring } = require('@polkadot/keyring');
const { hexToU8a } = require('@polkadot/util');
const { build_apikey, new_cert, encode_ssk, build_ssk } = require('@analog-labs/timegraph-wasm');
const { TimegraphClient } = require('@analog-labs/timegraph-js');

waitReady()
  .then(async() => {
    const keyring = new Keyring({ type: 'sr25519' });
    const keypair = keyring.addFromSeed(hexToU8a("0x0e5751c026e543b2e8ab2eb06099daa1d1e5df47778f7787faab45cdf12fe3a8"));

    const [cert_data, secret] = new_cert(keypair.address, "developer");

    // Sign the certificate data with the keypair
    const signature = keypair.sign(cert_data);

    // Build the API key using the secret, certificate data, and signature
    const api_key = build_apikey(secret, cert_data, signature );
    const ssk_data = encode_ssk({
        ns: 0,
      
        key: keypair.address,
        user_d: 1,
        expiration : 0
    });
    const ssk_sign = keypair.sign(ssk_data)
    const build_data = build_ssk(ssk_data, ssk_sign)


    console.log("cert_data", cert_data);
    console.log("my api key", api_key);
    console.log(keyring);
    console.log("api_Data", build_data);

      // Initialize TimegraphClient with the provided URL and session key
      const client = new TimegraphClient({
        url: "https://timegraph.staging.analog.one",
        sessionKey: api_key
      });
  
      // Create a user using the TimegraphClient
      const user = await client.user.create({
        address: keypair.address
      });
      const authenticate = await client.apiKey.certify({
        cert: key.cert
      })
      console.log("User created:", user);
      console.log("authentication", authenticate)
  })
  .catch((error) => {
    console.error('Error initializing WASM interface:', error);
  });


  /* 
  
  create database customer_database;
use customer_database;
show databases;

create table customers_account(
Name VARCHAR(50) not null,
P_id int primary key ,
City VARCHAR(100) NOT NULL,
Account_number int ,
Age int not null,
Post_code int not null

);
select * from customers_account;
insert into customers_account values("caleb", 001, "london", 0243201274, 26, 400242);
  
  */