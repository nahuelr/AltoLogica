# AltoLogica
Create an endpoint to return the prime numbers from a list.
Test are out of the scope.

- Endpoint: http://127.0.0.1:8000/api/numbers/get_prime/

- Method Allowed: `POST, OPTIONS`
- Body format: `{"numbers": [\<list of numbers\>]}`
- Response format: 
    - `{"prime_numbers": [\<list of prime numbers\>]}` if the request is successful
    - `{"error": "error message"}` if the request is not successful
    - method not allowed (`405`) if the method is not POST or OPTIONS
- Body example: `{"numbers": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- Response example: `{"prime_numbers": [2, 3, 5, 7]}`

## How to run the project
1. Clone the repository
2. Create a virtual environment using poetry
3. Install the dependencies
    ```bash
    poetry shell
    poetry install
    ```
4. Run the project
    ```bash
    python manage.py runserver
    ```
5. Access the endpoint using the browser or a tool like Postman

### Note
It is build using django rest framework, so you can use the browsable api from the directly from the browser.