from sklearn.ensemble import IsolationForest

clf = IsolationForest(n_estimators=50, max_samples=50,
                      contamination=float(0.004),
                      max_features=1.0,
                      bootstrap=False,
                      n_jobs=-1.
                      random_state = None,
                      verbose =0,
                      behaviour = "new")
