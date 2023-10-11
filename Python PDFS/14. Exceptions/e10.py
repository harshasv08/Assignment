try:
    import non_existent_module 
except ModuleNotFoundError as e:
    print(f"Module Not Found Error: {e}")
