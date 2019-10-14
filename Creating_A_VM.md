# Running Good-Grub in Python Virtual Environment

<!-- toc -->

To run Good-Grub in Python virtual environment follow the steps:

1. Install `virtualenv` package:

   ```sh
   pip install virtualenv
   ```

2. Create virtual environment (replace `my-Grub-env` with
   your virtual environment name):

   ```sh
   virtualenv my-Grub-env
   ```

3. Activate the environment.
   1. For Windows run

      ```sh
      my-Grub-env\Scripts\activate
      ```

   2. For Linux and Mac run

      ```sh
      source my-Grub-env/bin/activate
      ```

4. Run Good-Grub:

   ```sh
   cd Good-Grub
   ```

5. To deactivate virtual environment run:

   ```sh
   deactivate
   ```

## Still stumped ??
The documentation for installing VM: https://virtualenv.pypa.io/en/latest/installation/
