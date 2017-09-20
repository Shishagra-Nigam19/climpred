"""
Simply a bunch of NCL colormaps. Most of this script is constant colormap
arrays and then one simple function to load them.

- `load_cmap` : Function to load in a non-matplotlib/cmocean colormap.

"""
import numpy as np
import esmtools.vis as vis
import pandas as pd
import matplotlib.colors as color

def load_cmap(name):
    """
    Returns a colormap to use in plotting.

    Parameters
    ----------
    name : str
        Identifier for colormap.
    """
    df = pd.DataFrame(eval(name))
    cmap = color.ListedColormap(df.values)
    return cmap

# COLORMAPS

# Rainbow
# ------

# 1. AMWG
amwg = np.array([[ 0.57254902,  0.43921569,  0.85882353],
       [ 0.55294118,  0.41568627,  0.85490196],
       [ 0.52941176,  0.39607843,  0.85098039],
       [ 0.50588235,  0.37254902,  0.84705882],
       [ 0.48235294,  0.35294118,  0.84313725],
       [ 0.45882353,  0.32941176,  0.83921569],
       [ 0.43529412,  0.30980392,  0.83529412],
       [ 0.41176471,  0.29019608,  0.83137255],
       [ 0.38431373,  0.27058824,  0.83137255],
       [ 0.36078431,  0.24705882,  0.82745098],
       [ 0.33333333,  0.22745098,  0.82352941],
       [ 0.30980392,  0.20784314,  0.81960784],
       [ 0.28235294,  0.18823529,  0.81568627],
       [ 0.25490196,  0.16862745,  0.81176471],
       [ 0.22745098,  0.14901961,  0.80784314],
       [ 0.2       ,  0.12941176,  0.80784314],
       [ 0.17254902,  0.10980392,  0.80392157],
       [ 0.14509804,  0.09019608,  0.8       ],
       [ 0.11372549,  0.07058824,  0.79607843],
       [ 0.08627451,  0.05490196,  0.79215686],
       [ 0.05882353,  0.03529412,  0.78823529],
       [ 0.02745098,  0.01568627,  0.78431373],
       [ 0.        ,  0.        ,  0.78431373],
       [ 0.00784314,  0.01568627,  0.78823529],
       [ 0.01568627,  0.03529412,  0.79215686],
       [ 0.02745098,  0.05098039,  0.8       ],
       [ 0.03529412,  0.07058824,  0.80392157],
       [ 0.04705882,  0.08627451,  0.80784314],
       [ 0.05490196,  0.10588235,  0.81568627],
       [ 0.06666667,  0.12156863,  0.81960784],
       [ 0.07843137,  0.14117647,  0.82352941],
       [ 0.08627451,  0.15686275,  0.83137255],
       [ 0.09803922,  0.17647059,  0.83529412],
       [ 0.10980392,  0.19607843,  0.84313725],
       [ 0.11764706,  0.21176471,  0.84705882],
       [ 0.12941176,  0.23137255,  0.85098039],
       [ 0.14117647,  0.24705882,  0.85882353],
       [ 0.15294118,  0.26666667,  0.8627451 ],
       [ 0.16470588,  0.28235294,  0.86666667],
       [ 0.17254902,  0.30196078,  0.8745098 ],
       [ 0.18431373,  0.31764706,  0.87843137],
       [ 0.19607843,  0.3372549 ,  0.88235294],
       [ 0.20784314,  0.35294118,  0.89019608],
       [ 0.21960784,  0.37254902,  0.89411765],
       [ 0.23529412,  0.38823529,  0.90196078],
       [ 0.24313725,  0.4       ,  0.90196078],
       [ 0.25490196,  0.41176471,  0.90588235],
       [ 0.2627451 ,  0.41960784,  0.90588235],
       [ 0.2745098 ,  0.43137255,  0.90980392],
       [ 0.28627451,  0.43921569,  0.90980392],
       [ 0.29411765,  0.45098039,  0.91372549],
       [ 0.30588235,  0.45882353,  0.91372549],
       [ 0.31764706,  0.47058824,  0.91764706],
       [ 0.3254902 ,  0.47843137,  0.91764706],
       [ 0.3372549 ,  0.49019608,  0.92156863],
       [ 0.34901961,  0.49803922,  0.9254902 ],
       [ 0.36078431,  0.50980392,  0.9254902 ],
       [ 0.36862745,  0.51764706,  0.92941176],
       [ 0.38039216,  0.52941176,  0.92941176],
       [ 0.39215686,  0.5372549 ,  0.93333333],
       [ 0.40392157,  0.54901961,  0.93333333],
       [ 0.41176471,  0.55686275,  0.9372549 ],
       [ 0.42352941,  0.56862745,  0.9372549 ],
       [ 0.43529412,  0.57647059,  0.94117647],
       [ 0.44705882,  0.58823529,  0.94117647],
       [ 0.45882353,  0.59607843,  0.94509804],
       [ 0.47058824,  0.60784314,  0.94901961],
       [ 0.47843137,  0.62745098,  0.94509804],
       [ 0.49019608,  0.64313725,  0.94117647],
       [ 0.50196078,  0.6627451 ,  0.94117647],
       [ 0.50980392,  0.67843137,  0.9372549 ],
       [ 0.52156863,  0.69803922,  0.9372549 ],
       [ 0.52941176,  0.71372549,  0.93333333],
       [ 0.54117647,  0.72941176,  0.93333333],
       [ 0.55294118,  0.74117647,  0.92941176],
       [ 0.56078431,  0.75686275,  0.92941176],
       [ 0.57254902,  0.76862745,  0.9254902 ],
       [ 0.58039216,  0.78431373,  0.9254902 ],
       [ 0.59215686,  0.79607843,  0.92156863],
       [ 0.6       ,  0.80392157,  0.91764706],
       [ 0.61176471,  0.81568627,  0.91764706],
       [ 0.61960784,  0.82745098,  0.91372549],
       [ 0.63137255,  0.83529412,  0.91372549],
       [ 0.63921569,  0.84313725,  0.90980392],
       [ 0.65098039,  0.85098039,  0.90980392],
       [ 0.65882353,  0.85882353,  0.90588235],
       [ 0.67058824,  0.86666667,  0.90588235],
       [ 0.67843137,  0.87058824,  0.90196078],
       [ 0.69019608,  0.87843137,  0.90196078],
       [ 0.68627451,  0.87843137,  0.90588235],
       [ 0.68235294,  0.88235294,  0.90980392],
       [ 0.67843137,  0.88627451,  0.91372549],
       [ 0.6745098 ,  0.89019608,  0.91764706],
       [ 0.67058824,  0.89411765,  0.92156863],
       [ 0.66666667,  0.89803922,  0.92941176],
       [ 0.65882353,  0.90196078,  0.93333333],
       [ 0.65490196,  0.90588235,  0.9372549 ],
       [ 0.65098039,  0.90980392,  0.94117647],
       [ 0.64705882,  0.91372549,  0.94509804],
       [ 0.64313725,  0.91764706,  0.95294118],
       [ 0.63921569,  0.92156863,  0.95686275],
       [ 0.63529412,  0.9254902 ,  0.96078431],
       [ 0.62745098,  0.92941176,  0.96470588],
       [ 0.62352941,  0.93333333,  0.96862745],
       [ 0.61960784,  0.9372549 ,  0.97647059],
       [ 0.61568627,  0.94117647,  0.98039216],
       [ 0.60784314,  0.94509804,  0.98431373],
       [ 0.60392157,  0.94901961,  0.98823529],
       [ 0.6       ,  0.95294118,  0.99215686],
       [ 0.59607843,  0.96078431,  1.        ],
       [ 0.59607843,  0.97254902,  0.98823529],
       [ 0.6       ,  0.97647059,  0.96470588],
       [ 0.6       ,  0.96470588,  0.92941176],
       [ 0.60392157,  0.95294118,  0.89411765],
       [ 0.60392157,  0.94117647,  0.8627451 ],
       [ 0.60392157,  0.92941176,  0.83529412],
       [ 0.60784314,  0.91764706,  0.80784314],
       [ 0.60784314,  0.90588235,  0.78039216],
       [ 0.60784314,  0.89411765,  0.75686275],
       [ 0.60784314,  0.88235294,  0.73333333],
       [ 0.60784314,  0.87058824,  0.70980392],
       [ 0.60784314,  0.85882353,  0.69019608],
       [ 0.60784314,  0.84705882,  0.67058824],
       [ 0.60784314,  0.83529412,  0.65098039],
       [ 0.60784314,  0.82352941,  0.63529412],
       [ 0.60784314,  0.81176471,  0.61960784],
       [ 0.60784314,  0.80392157,  0.60784314],
       [ 0.96078431,  0.90196078,  0.74509804],
       [ 0.95294118,  0.89019608,  0.72941176],
       [ 0.94901961,  0.88235294,  0.71764706],
       [ 0.94117647,  0.87058824,  0.70196078],
       [ 0.9372549 ,  0.85882353,  0.69019608],
       [ 0.93333333,  0.85098039,  0.67843137],
       [ 0.9254902 ,  0.83921569,  0.6627451 ],
       [ 0.92156863,  0.83137255,  0.65098039],
       [ 0.91764706,  0.81960784,  0.63921569],
       [ 0.90980392,  0.80784314,  0.62352941],
       [ 0.90588235,  0.79607843,  0.61176471],
       [ 0.90196078,  0.78823529,  0.6       ],
       [ 0.89411765,  0.77647059,  0.58823529],
       [ 0.89019608,  0.76470588,  0.57647059],
       [ 0.88627451,  0.75294118,  0.56470588],
       [ 0.87843137,  0.74117647,  0.55294118],
       [ 0.8745098 ,  0.72941176,  0.54117647],
       [ 0.87058824,  0.72156863,  0.52941176],
       [ 0.8745098 ,  0.71764706,  0.50588235],
       [ 0.88235294,  0.71764706,  0.48235294],
       [ 0.88627451,  0.72156863,  0.4627451 ],
       [ 0.89411765,  0.72156863,  0.43921569],
       [ 0.89803922,  0.7254902 ,  0.41568627],
       [ 0.90588235,  0.72941176,  0.39215686],
       [ 0.91372549,  0.73333333,  0.36862745],
       [ 0.91764706,  0.7372549 ,  0.34509804],
       [ 0.9254902 ,  0.74117647,  0.32156863],
       [ 0.92941176,  0.74901961,  0.29411765],
       [ 0.9372549 ,  0.75686275,  0.27058824],
       [ 0.94117647,  0.76470588,  0.24313725],
       [ 0.94901961,  0.77254902,  0.21960784],
       [ 0.95686275,  0.78431373,  0.19215686],
       [ 0.96078431,  0.79607843,  0.16470588],
       [ 0.96862745,  0.80784314,  0.1372549 ],
       [ 0.97254902,  0.81960784,  0.10980392],
       [ 0.98039216,  0.83137255,  0.08235294],
       [ 0.98431373,  0.84705882,  0.05490196],
       [ 0.99215686,  0.8627451 ,  0.02745098],
       [ 1.        ,  0.88235294,  0.        ],
       [ 1.        ,  0.87058824,  0.        ],
       [ 1.        ,  0.85882353,  0.        ],
       [ 1.        ,  0.84705882,  0.        ],
       [ 1.        ,  0.83921569,  0.        ],
       [ 1.        ,  0.82745098,  0.        ],
       [ 1.        ,  0.81568627,  0.        ],
       [ 1.        ,  0.80392157,  0.        ],
       [ 1.        ,  0.79607843,  0.        ],
       [ 1.        ,  0.78431373,  0.        ],
       [ 1.        ,  0.77254902,  0.        ],
       [ 1.        ,  0.76470588,  0.        ],
       [ 1.        ,  0.75294118,  0.        ],
       [ 1.        ,  0.74117647,  0.        ],
       [ 1.        ,  0.72941176,  0.        ],
       [ 1.        ,  0.72156863,  0.        ],
       [ 1.        ,  0.70980392,  0.        ],
       [ 1.        ,  0.69803922,  0.        ],
       [ 1.        ,  0.68627451,  0.        ],
       [ 1.        ,  0.67843137,  0.        ],
       [ 1.        ,  0.66666667,  0.        ],
       [ 1.        ,  0.65490196,  0.        ],
       [ 1.        ,  0.64705882,  0.        ],
       [ 1.        ,  0.62745098,  0.        ],
       [ 1.        ,  0.61176471,  0.        ],
       [ 1.        ,  0.59215686,  0.        ],
       [ 1.        ,  0.57647059,  0.        ],
       [ 1.        ,  0.56078431,  0.        ],
       [ 1.        ,  0.54117647,  0.        ],
       [ 1.        ,  0.5254902 ,  0.        ],
       [ 1.        ,  0.50980392,  0.        ],
       [ 1.        ,  0.49019608,  0.        ],
       [ 1.        ,  0.4745098 ,  0.        ],
       [ 1.        ,  0.45882353,  0.        ],
       [ 1.        ,  0.43921569,  0.        ],
       [ 1.        ,  0.42352941,  0.        ],
       [ 1.        ,  0.40392157,  0.        ],
       [ 1.        ,  0.38823529,  0.        ],
       [ 1.        ,  0.37254902,  0.        ],
       [ 1.        ,  0.35294118,  0.        ],
       [ 1.        ,  0.3372549 ,  0.        ],
       [ 1.        ,  0.32156863,  0.        ],
       [ 1.        ,  0.30196078,  0.        ],
       [ 1.        ,  0.28627451,  0.        ],
       [ 1.        ,  0.27058824,  0.        ],
       [ 0.98431373,  0.25882353,  0.00784314],
       [ 0.97254902,  0.25098039,  0.01568627],
       [ 0.95686275,  0.24313725,  0.02352941],
       [ 0.94509804,  0.23137255,  0.03137255],
       [ 0.92941176,  0.22352941,  0.03921569],
       [ 0.91764706,  0.21568627,  0.04705882],
       [ 0.90196078,  0.20784314,  0.05490196],
       [ 0.89019608,  0.20392157,  0.05882353],
       [ 0.8745098 ,  0.19607843,  0.06666667],
       [ 0.8627451 ,  0.18823529,  0.0745098 ],
       [ 0.84705882,  0.18431373,  0.07843137],
       [ 0.83529412,  0.17647059,  0.08627451],
       [ 0.81960784,  0.17254902,  0.09019608],
       [ 0.80784314,  0.16470588,  0.09803922],
       [ 0.79215686,  0.16078431,  0.10196078],
       [ 0.78039216,  0.15686275,  0.10588235],
       [ 0.76470588,  0.15294118,  0.10980392],
       [ 0.75294118,  0.14509804,  0.11764706],
       [ 0.7372549 ,  0.14117647,  0.12156863],
       [ 0.7254902 ,  0.1372549 ,  0.1254902 ],
       [ 0.70980392,  0.13333333,  0.12941176],
       [ 0.69803922,  0.13333333,  0.13333333],
       [ 0.70980392,  0.14901961,  0.14901961],
       [ 0.7254902 ,  0.16862745,  0.16862745],
       [ 0.7372549 ,  0.19215686,  0.19215686],
       [ 0.75294118,  0.21176471,  0.21176471],
       [ 0.76470588,  0.23137255,  0.23137255],
       [ 0.78039216,  0.25490196,  0.25490196],
       [ 0.79215686,  0.27843137,  0.27843137],
       [ 0.80784314,  0.30196078,  0.30196078],
       [ 0.81960784,  0.3254902 ,  0.3254902 ],
       [ 0.83529412,  0.34901961,  0.34901961],
       [ 0.84705882,  0.37647059,  0.37647059],
       [ 0.8627451 ,  0.4       ,  0.4       ],
       [ 0.8745098 ,  0.42745098,  0.42745098],
       [ 0.89019608,  0.45490196,  0.45490196],
       [ 0.90196078,  0.48235294,  0.48235294],
       [ 0.91764706,  0.50980392,  0.50980392],
       [ 0.92941176,  0.54117647,  0.54117647],
       [ 0.94509804,  0.57254902,  0.57254902],
       [ 0.95686275,  0.6       ,  0.6       ],
       [ 0.97254902,  0.63137255,  0.63137255],
       [ 0.98431373,  0.6627451 ,  0.6627451 ],
       [ 1.        ,  0.69803922,  0.69803922]])
