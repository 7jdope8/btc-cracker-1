package main

import (
    "os"
    "fmt"
    "flag"
    "encoding/hex"
    "crypto/aes"
    "crypto/sha512"
    "crypto/sha256"
    "crypto/cipher"

    "github.com/ethereum/go-ethereum/crypto/secp256k1"
)

type ConfigWallet struct {
	Salt             string
	DeriveIterations uint32
	Crypted_key      string
	Ckey             string
	Pubkey           string
}

var walletOptions = ConfigWallet {
    Salt: "ebd46cea1e816bc2",
    DeriveIterations: 78519,
    Crypted_key: "16c291d1d271ce7afbe7cef3dc74623a8a72f830dccbc109a6d1c3ec8bca3ffe2f10aa4afe0998d871462e255273a96e",
    Ckey: "ec7e4b2084f57ba4cb191a4ff977e735c1a1b371ab6bfd7f390b11731cc71691da580d5a16779e46b1dcba92e0ab3d2b",
    Pubkey: "458167977091317582f1dea6b202fb44edb4f33907f0760c6bfb55c0ca6131a8",
}

var m_pubkey_hash = GetPubkeyHash()

var m_curve = secp256k1.S256()

// Calc pubkey hash
func GetPubkeyHash() []byte {
    pubkey_bc, _ := hex.DecodeString("03" + walletOptions.Pubkey)
    data := sha256.Sum256(pubkey_bc)
    data = sha256.Sum256(data[:])
    return data[:]
}

// Generate private key
func GenPrivateKey(password string) []byte {
    salt, _ := hex.DecodeString(walletOptions.Salt)
    data := sha512.Sum512([]byte(password + string(salt)))
    for i := uint32(1); i < walletOptions.DeriveIterations; i++ {
        data = sha512.Sum512(data[:])
    }
    chKey := data[0:32]
    chIV := data[32:48]

    block, _ := aes.NewCipher(chKey)
    cbc := cipher.NewCBCDecrypter(block, chIV)
    crypted_key, _ := hex.DecodeString(walletOptions.Crypted_key)
    cbc.CryptBlocks(crypted_key, crypted_key)

    chKey = crypted_key[0:32]
    chIV = m_pubkey_hash[0:16]

    block, _ = aes.NewCipher(chKey)
    cbc = cipher.NewCBCDecrypter(block, chIV)
    ckey, _ := hex.DecodeString(walletOptions.Ckey)
    cbc.CryptBlocks(ckey, ckey)

    return ckey[0:32]
}


// Check password
func CheckPassword(password string) bool {
    secret := GenPrivateKey(password)
    x, _ := m_curve.ScalarBaseMult(secret)
    return x.Text(16) == walletOptions.Pubkey
}

func main() {
    flag.Parse()
    if flag.NArg() == 0 {
        fmt.Printf("Usage: %s password\n", os.Args[0])
        os.Exit(1)
    }

    password := flag.Args()[0]
    fmt.Printf("%s: %t\n", password, CheckPassword(password))
}