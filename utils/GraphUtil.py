#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu Nguyen" at 00:51, 29/03/2020                                                        %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Thieu_Nguyen6                                  %
#       Github:     https://github.com/thieunguyen5991                                                  %
# -------------------------------------------------------------------------------------------------------%

#import matplotlib as mpl
#mpl.use('Agg')
import matplotlib.pyplot as plt


def draw_predict(y_test=None, y_pred=None, filename=None, pathsave=None):
    plt.plot(y_test)
    plt.plot(y_pred)
    plt.ylabel('CPU')
    plt.xlabel('Timestamp')
    plt.legend(['Actual', 'Predict'], loc='upper right')
    plt.savefig(pathsave + filename + ".png")
    plt.close()
    return None


def draw_predict_with_error(data=None, error=None, filename=None, pathsave=None):
    plt.plot(data[0])
    plt.plot(data[1])
    plt.ylabel('Real value')
    plt.xlabel('Point')
    plt.legend(['Predict y... RMSE= ' + str(error[0]), 'Test y... MAE= ' + str(error[1])], loc='upper right')
    plt.savefig(pathsave + filename + ".png")
    plt.close()
    return None


def draw_raw_time_series_data(data=None, label=None, title=None, filename=None, pathsave=None):
    plt.plot(data)
    plt.xlabel(label["y"])
    plt.ylabel(label["x"])
    plt.title(title, fontsize=8)
    plt.savefig(pathsave + filename + ".pdf")
    plt.close()
    return None


def draw_raw_time_series_data_and_show(data=None, label=None, title=None):
    plt.plot(data)
    plt.xlabel(label["y"])
    plt.ylabel(label["x"])
    plt.title(title, fontsize=8)
    plt.show()
    return None

