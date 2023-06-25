from ..models.BiometricData import BiometricData

class BiometricData_collection(BiometricData):

    def __init__(self, biometric_data_ID=0):
        self._biometric_data_ID = biometric_data_ID

    def set_biometric_data_id(self, biometric_data_ID: int):
        self._biometric_data_ID = biometric_data_ID
    
    def get_biometric_data_id(self):
        return self._biometric_data_ID
    
    def get(self):
        biometric_data = BiometricData.query.filter_by(id=self._biometric_data_ID).first()

        return biometric_data if biometric_data else None

    def all():
        biometric_datas = BiometricData.query.all()

        return biometric_datas if biometric_datas else []