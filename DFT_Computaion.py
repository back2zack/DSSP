import numpy as np
import numpy.fft as fft 
import scipy.signal as sig
import matplotlib.pyplot as plt



# first we creat a sinple  signal 
N = 2**10 #  totall number of samples 
f = 1000 #  frequency of the signal  , how  many times it repeats it self per second 
fs = 8000 #  sampling frequency the number of samples per second 
Ts = 1/fs # sampling period 

t = np.r_[0:N*Ts:Ts]
x = np.sin((2*np.pi*f)*t)
plt.plot(t[t < 0.02]*1000, x[t < 0.02]);
plt.xlim((0, 20))
plt.grid(True)
plt.xlabel(r'$t\ /\ \mathrm{ms}$')
plt.title("First 20 ms of signal x(t)",
          fontsize=14);


# our signal x is a real valued signal 
# we want to compute the DFT of the 2M point  real signal 
# by computing the DFT of a complex signal with half the lenth (M) 
def re_fft(x):
    # make sufe the signal have an even nmber of sample points 
    if x.shape[0] % 2 != 0 :
        raise ValueError("pleasae give a signal with an even number of sample points")
    if np.iscomplexobj(x):
        raise ValueError("the signal should be a real valued signal")
    # convert a real _valued signal into an complex valued signal  
    y = x.view(dtype= np.complex128)

    # convert to F
    Y = fft.fft(y)
    print(len(Y))

    # by looking  at the len Y deosn t have the midel point M yet
    # let s append it first 
    M = len(x) // 2 # we know that X(M)= X(0)
    Y = np.append(Y, Y[0])
    Y_1 = 1/2*(Y + Y[::-1].conj())
    Y_2 = 1/2j*(Y - Y[::-1].conj())

    # now we have a representation of the Complex signal that has only M points
    # in the frequency domain 
    # now lets calculate the DFT of x using this representation
    # we know X = Y_1 + Y_2 * exp(-j*np.pi/M)

    X = Y_1 + np.exp(-1j*np.pi*np.r_[0:M+1]/M) * Y_2 

    # but till now we calculated just half of the X --> 
    # we know that X[k] = k[M-k].conj()
    # so we just need to append the reverse conj of X to X
    right_X =  X[1:M][::-1]
    X = np.append(X, np.flipud(X[1:M]).conj())

    return X



def plt_magnitude():
    # calculate reference fft and own implementation
    X_ref = fft.fft(x)
    X_test = re_fft(x)

    # plot the results
    plt.figure()
    plt.subplot(3, 1, 1)
    plt.plot(abs(X_ref))
    plt.title('"Ordinary" FFT (M-point)', fontsize=16)

    plt.subplot(3, 1, 2)
    plt.plot(abs(X_test))
    plt.title('re_fft (2 times M/2-points)', fontsize=16)

    plt.subplot(3, 1, 3)
    plt.plot(abs(X_test-X_ref))
    plt.title('Error', fontsize=16)

    plt.gcf().subplots_adjust(hspace=0.5)
    plt.gcf().set_size_inches(14, 8)
    [ax.set_xlim((0, 1024)) and ax.set_xlabel(r'$k$', fontsize=14)
    for ax in plt.gcf().get_axes()]

    # Calculate the error
    error_rel_fft = np.linalg.norm(X_test - X_ref)**2/np.linalg.norm(X_ref)**2
    print("Relative quadratic error: {:e}".format(error_rel_fft))
    plt.show()

plt_magnitude()