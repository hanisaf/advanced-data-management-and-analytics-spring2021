# pytest


### Presentation
- 'https://youtu.be/UNl5oz0ZbQk' - this youtube link will be attached to the submission.
- 'Pytest Presentation.pptx' - this presentation is linked with my demo and gives more insight about pytest and its functions.

### Summary of Support Files

- `pytestdemo.ipynb`: this notebook contains the code for the demo.

### Guide

[Pytest] (https://docs.pytest.org/en/6.2.x/getting-started.html) - 
    this guide gives you all the information required to install Pytest and how the package expo works throughout python using a system like Terminal.
[Pytest] (iPytest): (https://pypi.org/project/ipytest/) -
    this guide give you information on how pytest can be simulated through Jupyter Notebook and how the function would work in a notebook setting.
    
    
 #### Introduction to ipytest:
   Pytest: 
        -is a framework that makes building simple and scalable tests easy. Tests are readable and very detailed. 
        -Features: gives details in-regards-to the assert function.
   Ipytest: 
        -support for pytest inside notebooks.
        -tight integration with IPython via magics and automatic code transforms
   
   #### Features
        - ipytest gives a simple interface
        - has support for pandas and numpy
        - builds on standard unit test.
   
   #### Pytest Functions:
        *-run_pytest[clean]
            Same as the %%run_pytest, but cleans any previously found tests, i.e., only tests defined in the current cell are   executed. To register the magics, run ipytest.config.magics = True first.
        -ipytest.config
            lets you run other methods of the config function. These include the ipytest.config.clean which lets you clean all the variables.
        *-ipytest.exit_code()
            this function returns the code of the last 
        *-ipytest.run()
            this function executes all tests in the the passed module
        -ipytest.clean_tests
            this function deletes tests with names matching the given pattern.
        -ipytest.reload
            this function reloads all modules passed as strings
        -ipytest.running_as_test()
            this fuction checks whether the notebook is executed as a test.
            this function may be useful, when running notebooks as integration tests to ensure the runtime is not very long.
        
            - the functions with stars are demo'd in my pytestdemo, I go more insight on these functions under the ipytest.autoconfig() function.
            
 #### Conclusion:
     -Overall in this package_expo, I've learned that Pytest with terminal and ipytest with jupyter in notebook is very helpful when running long amounts of code. If the user were to use long amounts of code and the assert function, then the %%run_pytest function. ipytest would show where code is wrong and it will tell you how to fix it.
