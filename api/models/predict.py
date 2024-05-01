import pickle

def predict(crop, start_date='2024-01-30', end_date='2024-12-31'):
    with open(f'models\\{crop}.pkl', 'rb') as file:
        arima_model = pickle.load(file)
    # Make predictions using the loaded model
    # Replace 'test_data' with your test data
    # predictions = arima_model.predict(n_periods=len(test_data))
    pred2 = arima_model.get_forecast('2026-12-31')
    pred2_ci = pred2.conf_int()
    # print(pred2.predicted_mean['2021-11-24':'2024-12-31'])
    # print(pred2.predicted_mean['2021-11-24':'2024-12-31'].to_list())
    return pred2.predicted_mean[start_date:end_date].to_list()

if __name__ == '__main__':
    predict('wheat')