from app.models.BiometricScore import BiometricScore

class BiometricScore_collection(BiometricScore):
    
    def __init__(self, biometric_score_ID=0):
        self._biometric_score_ID = biometric_score_ID

    def set_biometric_score_id(self, biometric_score_ID: int):
        self._biometric_score_ID = biometric_score_ID
    
    def get_biometric_score_id(self):
        return self._biometric_score_ID
