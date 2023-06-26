import math


class BiometricData:

    def __init__(
            self,
            age: int,
            height: float,
            weight: float,
            gender: str
    ):

        self._age = int(age)
        self._height = float(height)
        self._height_m = float(float(height) / 100)
        self._weight = float(weight)
        self._gender = str(gender)

    """
    A function that calculate BMI (Body Mass Index) and return it.

    Parameters:
        weight  (float) : Person weight in kg.
        height  (float) : Person height in m.

    Returns:
        float: BMI score.
    """

    def calculate_BMI(self):

        bmi = self._weight / (self._height_m ** 2)

        self._bmi = bmi

        return round(bmi, 2)

    """
        A function that calculate BMR (Basal Metabolic Rate) and return it.

        Parameters:
            weight  (float) : Person weight in kg.
            height    (int) : Person height in cm.
            age       (int) : Person age in years.

        Returns:
            float: BMR score.
    """

    def calculate_BMR(self):

        if self._gender == 'Female':
            x = -161
        else:
            x = 5

        bmr = 10 * self._weight + 6.25 * self._height - 5 * self._age + x

        return round(bmr, 2)

    """
        A function that calculate PBF (Percent Body Fat) and return it.

        Parameters:
            waist_circumference     (int) : Person waist circumference in cm.
            hip_circumference       (int) : Person hip circumference in cm.
            neck_circumference      (int) : Person neck circumference in cm.
            height                (float) : Person height in cm.

        Returns:
            float: PBF score.
    """

    def calculate_PBF(self):

        if self._gender == 'Female':
            pbf = (0.25 * self._weight) + 0.7
        else:
            pbf = (0.15 * self._weight) + 0.7

        return round(pbf, 2)

    """
        A function that calculate FFM (Fat-Free Mass) and return it.

        Parameters:
            height  (float) : Person height in cm.
            weight  (float) : Person weight in kg.
            age       (int) : Person age in years.

        Returns:
            float: FFM score.
    """

    # def calculate_FFM(self):

    #     brm = BiometricData.calculate_BMR()

    #     ffm = self._weight - (self._weight * )

    #     return round(ffm, 2)

    def calculate_fit_score(self):

        fitscore = 0

        if self._height >= 180:
            fitscore = 15
        elif self._height >= 170:
            fitscore = 10
        elif self._height >= 160:
            fitscore = 5
        else:
            fitscore = 0

        if self._weight <= 70:
            fitscore += 15
        elif self._weight <= 80:
            fitscore += 10
        elif self._weight <= 90:
            fitscore += 5
        else:
            fitscore += 0

        if self._age <= 30:
            fitscore += 10
        elif self._age <= 40:
            fitscore += 5
        else:
            fitscore += 0

        if self._gender == 'Male':
            fitscore += 5
        elif self._gender == 'Female':
            fitscore += 0

        if self._bmi <= 18.5:
            fitscore += 5
        elif self._bmi <= 24.9:
            fitscore += 10
        elif self._bmi <= 29.9:
            fitscore += 7
        else:
            fitscore += 0

        fitscore = (fitscore / 70) * 100

        return fitscore
