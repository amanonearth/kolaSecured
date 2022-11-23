const process = require("process");
const fs = require('fs');
const pinataSDK = require('@pinata/sdk');
const PINATA_API_KEY = '4accfd14a7a3d1d4d719';
const PINATA_SECRET_API_KEY = '80f01b0073ecf5d4b8cbf1a811373b4579fa984fb75ff9a24fa5e07e692b8598';

const pinata = new pinataSDK(PINATA_API_KEY, PINATA_SECRET_API_KEY);

var imgPath = process.argv[2]
const readableStreamForFile = fs.createReadStream(imgPath);
// const options = {};
const options = {
    pinataMetadata: {
        name: 'Test',
    },
    pinataOptions: {
        cidVersion: 0
    }
};
console.log(imgPath);

pinata.pinFileToIPFS(readableStreamForFile, options).then((result) => {
    console.log(result["IpfsHash"])
}).catch((err) => {
    console.log(err)
});