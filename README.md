<!-- 
Keywords

Omkar Account Generator
name: omkar-account-generator
package_name: omkar_account_generator
description: Generate user accounts.
README.md:


-->


# Omkar Account Generator

Omkar Account Generator provides a convenient solution for creating accounts. It is particularly useful for automated tasks that require account creation in selenium.

## Getting Started
To get started with Omkar Account Generator install `omkar-account-generator` using the following command:

```bash
python -m pip install omkar-account-generator
```

## Usage

1. `generate_account(gender, country)`

Generates an account

**Parameters**
- `gender` (optional): The gender of the user account to generate. Value can be `Gender.MEN`, `Gender.WOMEN`, `Gender.BOTH`. Default's to `Gender.BOTH`
- `country` (optional): The country of the user account to generate. It accepts a value from the `Country` enum. The default value is `None`, which means the country can be any country.


**Example**
```python
from omkar_account_generator import AccountGenerator, Gender, Country

account = AccountGenerator.generate_account(gender = Gender.WOMEN, country=Country.IN)
print(account)
```

**Output**
```json

```

2. `generate_accounts(n, gender, country)`

Generates multiple user accounts.

**Parameters**

- `n`: The number of user accounts to generate.
- `gender` (optional): The gender of the user account to generate. Value can be `Gender.MEN`, `Gender.WOMEN`, `Gender.BOTH`. Default's to `Gender.BOTH`
- `country` (optional): The country of the user account to generate. It accepts a value from the `Country` enum. The default value is `None`, which means the country can be any country.


**Example**

```python
from omkar_account_generator import AccountGenerator, Gender, Country

accounts = AccountGenerator.generate_accounts(3, gender = Gender.WOMEN, country=Country.IN)
print(accounts)
```

**Output**

```json

```

## If my code helped you in creating accounts, please take a moment to [star the repository](https://github.com/omkarcloud/omkar-account-generator). Your act of starring will help developers in discovering our Repository and contribute towards helping fellow developers in their automation tasks. Dhanyawad 🙏! Vande Mataram!