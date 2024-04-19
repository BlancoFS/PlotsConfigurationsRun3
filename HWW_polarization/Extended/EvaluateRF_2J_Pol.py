# EvaluateRF_1J.py

import joblib
import numpy as np

rf_2_pol = joblib.load('/afs/cern.ch/work/s/sblancof/private/Run2Analysis/AlmaLinux9_mkShapes/mkShapesRDF/examples/extended/Training/random_forest_binary_2j_df_pol.pkl')

def load_random_forest_model_2jet_pol(inputs_2):
    try:
        result_pol_2_1 = rf_2_pol.predict_proba(np.array(inputs_2).reshape(1, -1))
        return [result_pol_2_1[0][1]]
    except Exception as e:
        return [-99.9, -99.9, -99.9]

if __name__ == "__main__":
    # You can include some test code here for local testing
    test_input = [1.0, 2.0, 3.0, 4., 5., 6., 7., 8., 9., 10., 11., 12., 13., 14., 15.]
    result = load_random_forest_model_2jet(test_input)
    print("Result:", result)
