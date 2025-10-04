class MyStatistic:
    def find_orders_within_range(df, minValue, maxValue):
        order_totals = df.groupby('OrderID').apply(lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum())
        orders_within_range = order_totals[(order_totals >= minValue) & (order_totals <= maxValue)]
        unique_orders = df[df['OrderID'].isin(orders_within_range.index)]['OrderID'].drop_duplicates().tolist()
        return unique_orders
    
    def find_orders_with_totals(df, minValue, maxValue, sorttype=True):
        order_totals = df.groupby('OrderID').apply(lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum())
        orders_within_range = order_totals[(order_totals >= minValue) & (order_totals <= maxValue)]
        if sorttype:
            orders_within_range = orders_within_range.sort_values(ascending=True)
        else:
            orders_within_range = orders_within_range.sort_values(ascending=False)
        result_df = orders_within_range.reset_index()
        result_df.columns = ['OrderID', 'Sum']
        return result_df