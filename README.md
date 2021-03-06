## Overview

Python library for leapchain digital currency.

This library contains all of the core logic, shared functionality, and
constants used by both the [Bank](https://github.com/LeapChain/Bank) and 
[Validator](https://github.com/LeapChain/Validator) on leapchain network.

## Project Setup

Follow the steps below to set up the project on your environment. If you run into any problems, feel free to leave a 
GitHub Issue or reach out to any of our communities above.

Install required packages:
```
pip3 install -e .
```

## Testing

To run tests:
```
pytest
```

To run tests with coverage report:
```
pytest --cov-config=.coveragerc --cov=./src 
```

To run linting:
```
flake8 .
```

## Building

The building and publishing of this package is automated through GitHub actions. To publish a new release, update the
`./src/leapchain/__init__.py` file with the latest version number. The updated package will be published once the
branch is merged into `master`.

To produce a source distribution manually:
```
python3 setup.py sdist
```

## License

leapchain is [MIT licensed](http://opensource.org/licenses/MIT).
