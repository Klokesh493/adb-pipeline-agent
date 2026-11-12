# Replay evidence

Captured stdout is compared with a checked-in baseline.

## Bundled scenario

Result: **PASS**

````text
{
  "retry": [
    "extract"
  ],
  "blocked": [
    "transform"
  ]
}
````

## Regression scenario

Result: **PASS**

````text
{
  "retry": [],
  "blocked": [
    "publish"
  ]
}
````
