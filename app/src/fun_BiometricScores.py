import math

class BiometricData:

    def __init__(self, data):
        self._age                    = data.age
        self._height                 = data.height
        self._weight                 = data.weight
        self._gender                 = data.sex
        self._bmi                    = data.BMI
        self._bmr                    = data.BMR
        self._pbf                    = data.PBF
        self._ffm                    = data.FFM
        self._waist_circumference    = data.waist_circumference
        self._hip_circumference      = data.hip_circumference
        self._neck_circumference     = data.neck_circumference

    """
    A function that calculate BMI (Body Mass Index) and return it.

    Parameters:
        weight (float)  : Person weight in kg.
        height (float)  : Person height in m.

    Returns:
        float: BMI score.
    """
    def calculate_BMI(self):

        bmi = self._weight / (self._height**2)

        return bmi

    """
        A function that calculate BMR (Basal Metabolic Rate) and return it.

        Parameters:
            weight (float)  : Person weight in kg.
            height (int)    : Person height in cm.
            age (int)       : Person age in years.

        Returns:
            float: BMR score.
    """
    def calculate_BMR(self):

        if self._gender == 'female':
            x = -161
        else:
            x = 5

        bmr = 10 * self._weight + 6.25 * self._height - 5 * self._age + x

        return bmr
    
    """
        A function that calculate PBF (Percent Body Fat) and return it.

        Parameters:
            waist_circumference (int)   : Person waist circumference in cm.
            hip_circumference (int)     : Person hip circumference in cm.
            neck_circumference (int)    : Person neck circumference in cm.
            height (float)              : Person height in cm

        Returns:
            float: PBF score.
    """
    def calculate_PBF(self):

        if self._gender == 'female':
            pbf = 495 / (1.0324 - 0.19077 * math.log10(self._waist_circumference - self._hip_circumference) + 0.15456 * math.log10(self._height)) - 450
        else:
            pbf = 495 / (1.29579 - 0.35004 * math.log10(self._waist_circumference + self._hip_circumference - self._neck_circumference) + 0.22100 * math.log10(self._height)) - 450

        return pbf
