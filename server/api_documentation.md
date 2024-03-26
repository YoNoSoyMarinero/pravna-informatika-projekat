## Case-Based Reasoning

This API endpoint allows users to perform case-based reasoning for legal judgments based on provided case base facts.

### Endpoint

- `/case_based_reasoning` - Perform case-based reasoning to retrieve similar cases. Uses annoy vector cosine similarity to find most similar vectors.

### Request Method

- **POST**

### Request Body

#### Example

```json
{
  "convicted": true,
  "self_usage": false,
  "marginalized_group": false,
  "providing_logistics": true,
  "married": true,
  "smuggling": false,
  "organized_group": true,
  "trafficking": false,
  "snitched": true,
  "admited": false,
  "great_amount_without_trafficking": true,
  "small_amount_without_trafficking": false,
  "allowed_usage": true,
  "has_children": true,
  "amount_of_cocaine": 10,
  "amount_of_heroine": 0,
  "amount_of_marijuana": 5
}
```

#### Parameters

- `convicted`: boolean (required) - Whether the defendant is convicted or not.
- `self_usage`: boolean (required) - Whether the defendant was using the substance themselves.
- `marginalized_group`: boolean (required) - Whether the defendant belongs to a marginalized group.
- `providing_logistics`: boolean (required) - Whether the defendant provided logistics for the illegal activity.
- `married`: boolean (required) - Whether the defendant is married.
- `smuggling`: boolean (required) - Whether the defendant was involved in smuggling.
- `organized_group`: boolean (required) - Whether the defendant was part of an organized group.
- `trafficking`: boolean (required) - Whether the defendant was involved in trafficking.
- `snitched`: boolean (required) - Whether the defendant snitched.
- `admited`: boolean (required) - Whether the defendant admitted to the crime.
- `great_amount_without_trafficking`: boolean (required) - Whether a large amount was involved without trafficking.
- `small_amount_without_trafficking`: boolean (required) - Whether a small amount was involved without trafficking.
- `allowed_usage`: boolean (required) - Whether the substance usage was allowed.
- `has_children`: boolean (required) - Whether the defendant has children.
- `amount_of_cocaine`: integer (required) - Amount of cocaine involved.
- `amount_of_heroine`: integer (required) - Amount of heroine involved.
- `amount_of_marijuana`: integer (required) - Amount of marijuana involved.

### Response

#### Success Response

```json
{
  "similar_cases": [
    {
      "case_id": "K 111/2019",
      "case_punishments": 24,
      "case_similarity": 0.8567573581363702
    },
    {
      "case_id": "K 18/2015",
      "case_punishments": 24,
      "case_similarity": 0.8531650288612651
    },
    {
      "case_id": "K 127/2013",
      "case_punishments": 30,
      "case_similarity": 0.8421311743088697
    }
  ]
}
```

#### Error Response

- **400 Bad Request**:
  - If the request body format is invalid.

## Rule-Based Reasoning

### Endpoint

- `/rule_based_reasoning` - Perform rule-based reasoning to generate a judgment. Uses dr-device to performe reasoning based on RuleML dialect.

### Request Method

- **POST**

### Request Body

#### Parameters

- `drug_posession`: bool (required) - Whether drug possession is involved.
- `allowing_usage`: bool (required) - Whether drug usage was allowed.
- `marginalized_group`: bool (required) - Whether the defendant belongs to a marginalized group.
- `providing_logistics`: bool (required) - Whether the defendant provided logistics for drug-related activities.
- `drug_trafficking`: bool (required) - Whether drug trafficking is involved.
- `smuggling`: bool (required) - Whether smuggling is involved.
- `organized_group`: bool (required) - Whether the defendant was part of an organized group.
- `article_52_violation`: bool (required) - Whether there's a violation of Article 52.
- `estimated_drug_price`: float (required) - Estimated drug price.

#### Example

```json
{
  "drug_posession": true,
  "allowing_usage": false,
  "marginalized_group": false,
  "providing_logistics": true,
  "drug_trafficking": false,
  "smuggling": false,
  "organized_group": true,
  "article_52_violation": true,
  "estimated_drug_price": 100.0
}
```

### Response

#### Success Response

```json
{
  "max_pen": ["36"],
  "min_pen": ["6"],
  "offenses": ["is_drug_posession_with_no_trafficking_lv1"]
}
```

#### Error Response

- **400 Bad Request**:
  - If the request body format is invalid.

## Endpoint

#### Get Legal documents

- **URL:** `/judgment`
- **Method:** `GET`
- **Parameters:**
  - `legal_document_name` (required): The name of the legal document to retrieve.
- **Response:**
  - `200 OK`: Returns the requested judgment document.
  - `400 Bad Request`: If the `legal_document_name` parameter is missing.
  - `404 Not Found`: If the requested document is not found.

### Endpoint

#### Get Law

- **URL:** `/law`
- **Method:** `GET`
- **Parameters:**
  - `legal_document_name` (required): The name of the legal document to retrieve.
- **Response:**
  - `200 OK`: Returns the requested law document.
  - `400 Bad Request`: If the `legal_document_name` parameter is missing.
  - `404 Not Found`: If the requested document is not found.
