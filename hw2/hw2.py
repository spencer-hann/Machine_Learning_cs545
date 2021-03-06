# This block checks for proper cython setup arguments
# you can provide your own if you want to test out different
# options and this block will be mainly ignored
import sys
print("======================================================================")
py_name = sys.argv[0]
module_name = sys.argv[0][:-3] # removes ".py"
cy_name = module_name + ".pyx"
if len(sys.argv) == 1: # no command line args
    print(cy_name + " compiling with default args")
    print("\tadding \"build_ext\" and \"--inplace\" to sys.argv")
    sys.argv.extend( ["build_ext", "--inplace"] )


# This block compiles/sets up the hw10 module
# from the  hw10.pyx cython file
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
print("   Cython may give a depricated NumPy API warning.")
print("   This warning is safe to ignore.\n")
setup(
    ext_modules = cythonize(
        Extension(
            module_name,
            [cy_name],
            define_macros=[("NPY_NO_DEPRECATED_API",None)]
        )
    )
)
print(module_name + " setup complete!")
print("======================================================================\n")


# This is where I import the pre-compiled 
# module and enter the Cython layer
from hw2 import * #change module name
if __name__ == "__main__":
    training_examples, training_targets = preprocess_data(
            "mnist_train.csv")#, max_rows=30000)
    testing_examples, testing_targets = preprocess_data(
            "mnist_test.csv")#, max_rows=2000)

    print("python:",sys.version)

    network10 = NN(n_hidden=10)
    network20 = NN(n_hidden=20)
    network100 = NN(n_hidden=100)#, momentum=0.0)

    data = (training_examples,training_targets,testing_examples,testing_targets)

#    acc_training, acc_testing = network10.speed_test(*data)
#    network10.plot_accuracy(acc_training, acc_testing)

    acc_training, acc_testing = network20.speed_test(*data)
    network20.plot_accuracy(acc_training, acc_testing)

    acc_training, acc_testing = network100.speed_test(*data)
    network100.plot_accuracy(acc_training, acc_testing)


#    # +1 for bias weight
#    n_hidden = 10 # 10, 20, 100
#    n_input = 1 + 784 # fixed
#    n_output = 10 # fixed
#    weights_x = np.random.rand(n_hidden, n_input)
#    weights_h = np.random.rand(n_output, n_hidden)
#    weights_x -= .5 # range was [0,1]
#    weights_h -= .5 # is now [-.5,.5]
#
#    print(get_accuracy(weights_x,weights_h,training_examples,training_targets))
