import joblib
import pprint

def inspect_file(file_path):
    print(f"\n--- Inspecting: {file_path} ---")
    
    try:
        obj = joblib.load(file_path)
        print("Type:", type(obj))

        if hasattr(obj, 'get_params'):
            pprint.pprint(obj.get_params())

        elif hasattr(obj, '__dict__'):
            pprint.pprint(obj.__dict__)

        else:
            pprint.pprint(obj)

        # Extra: If it's a StandardScaler
        if 'StandardScaler' in str(type(obj)):
            print("\nScaler Attributes:")
            print("Mean:", obj.mean_)
            print("Scale (std):", obj.scale_)
            print("Var:", obj.var_)
            print("Feature names (if available):", getattr(obj, 'feature_names_in_', 'N/A'))

    except Exception as e:
        print("Error loading file:", e)

# Inspect both files
inspect_file("torcs_mlp_model.pkl")
inspect_file("input_scaler.pkl")
