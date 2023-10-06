# Semgrep Rules And Our Evasive Strategies
## Our Motivation
[**Semgrep**](https://semgrep.dev/) is a fast, open source static analysis tool for finding bugs, detecting vulnerabilities. Different from traditional tools using regex to detecting secrets, Semgrep is more powerful. Its rule repository covers different programming languages. You can input the code snippets and scan them.

However based on some easy transformation on the vulnerable snippets, we can evade the analysis. So our work mainly focuses on proposing some kinds of strategies to evade the tool successfully while keeping the code snippets vulnewrable. Note that we choose _**Python**_ part as our target.

## Program Analysis
- String Matching (**SM**)
  - String Transformation (SM-1)
  - Type Conversion (SM-2)
  - Add/Remove Some Lines (SM-3)
- Constant Analysis (**CA**)
- Dataflow Analysis (**DA**)
  - Function Pointer (DA-1)
  - Function Call (DA-2)
- Taint Analysis (**TA**)

## Evasive Strategies
You can use `Ctrl + F` to search the rule and corresponding strategy you need. 

Note that some extended tranformation methods are given by [**ChatGPT 3.5**](https://chat.openai.com/) based on our manual effort (*). It is true this LLM model is a powerful tool to help us generate more changes on the code snippets to evade the program analysis tool while keeping them vulnerable.

| **No.** | **Category** | **Rule ID** | **Impact** | **Our Strategies** |
|:-------:|:------------:|:------------:|:----------:|:------------------:|
|   1     | cryptography | [empty-aes-key](https://semgrep.dev/orgs/nwpu/editor/r/python.cryptography.security.empty-aes-key.empty-aes-key) | High | [SM-1](./cryptography/empty-aes-key.md) |
|   2     | cryptography | [insecure-cipher-algorithm-arc4](https://semgrep.dev/orgs/nwpu/editor/r/python.cryptography.security.insecure-cipher-algorithms-arc4.insecure-cipher-algorithm-arc4) | Medium | [SM-3](./cryptography/insecure-cipher-algorithm-arc4.md) |
|   3     | cryptography | [insecure-cipher-algorithm-blowfish](https://semgrep.dev/orgs/nwpu/editor/r/python.cryptography.security.insecure-cipher-algorithms-blowfish.insecure-cipher-algorithm-blowfish) | Medium | [SM-3](./cryptography/insecure-cipher-algorithm-blowfish.md) |
|   4     | cryptography | [insecure-cipher-algorithm-idea](https://semgrep.dev/orgs/nwpu/editor/r/python.cryptography.security.insecure-cipher-algorithms.insecure-cipher-algorithm-idea) | Medium | [SM-3](./cryptography/insecure-cipher-algorithm-idea.md) |
|   5     | cryptography | [insecure-cipher-mode-ecb](https://semgrep.dev/orgs/nwpu/editor/r/python.cryptography.security.insecure-cipher-mode-ecb.insecure-cipher-mode-ecb) | Low | [SM-3](./cryptography/insecure-cipher-mode-ecb.md) |
|   6     | cryptography | [insecure-hash-algorithm-md5](https://semgrep.dev/orgs/nwpu/editor/r/python.cryptography.security.empty-aes-key.empty-aes-key) | Medium | [SM-1](./cryptography/insecure-hash-algorithm-md5.md) |
|   7     | cryptography | [insecure-hash-algorithm-sha1](https://semgrep.dev/orgs/nwpu/editor/r/python.cryptography.security.insecure-hash-algorithms.insecure-hash-algorithm-sha1) | Medium | [DA-1](./cryptography/insecure-hash-algorithm-sha1.md) |
|   8     | cryptography | [insufficient-dsa-key-size](https://semgrep.dev/orgs/nwpu/editor/r/python.cryptography.security.insufficient-dsa-key-size.insufficient-dsa-key-size) | Medium | [CA](./cryptography/insufficient-dsa-key-size.md) |
|   9     | cryptography | [insufficient-ec-key-size](https://semgrep.dev/orgs/nwpu/editor/r/python.cryptography.security.insufficient-ec-key-size.insufficient-ec-key-size) | Medium | [CA](./cryptography/insufficient-ec-key-size.md) |
|   10    | cryptography | [insufficient-rsa-key-size](https://semgrep.dev/orgs/nwpu/editor/r/python.cryptography.security.insufficient-rsa-key-size.insufficient-rsa-key-size) | Medium | [CA](./cryptography/insufficient-rsa-key-size.md) |
|   11    | cryptography | [crypto-mode-without-authentication](https://semgrep.dev/orgs/nwpu/editor/r/python.cryptography.security.mode-without-authentication.crypto-mode-without-authentication) | Medium | [SM-3](./cryptography/crypto-mode-without-authentication.md) |
