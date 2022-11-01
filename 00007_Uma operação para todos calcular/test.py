import pandas as pd

class Test(unittest.TestCase):
  def setUp(self):
    self.original = pd.DataFrame([{
        'cruise_id': 10404,
        'country_id': 19,
        'country': 'Brasil',
        'date': '2020-02-06',
        'date_id': 14646,
        'port_id': 2,
        'port': 'Punta del Este',
        'total_people': 2,
        'visits_amount': 2,
        'total_expenses': 1.0,
        'tours_expenses': 5.0,
        'feed_expenses': 0.0,
        'transport_expenses': 10.0,
        'shopping_expenses': 3.0,
        'other_expenses': 2.0}])
  
  def test_ajustar_gastos_retorna_uma_copia_da_tabela(self):
    self.assertTrue(ajustar_gastos(self.original, 1) is not self.original, "não deve retornar o mesmo dataframe, mas uma cópia")    

  def test_ajustar_gastos_com_1_retorna_uma_copia_identica_do_dataframe(self):
    self.assertEquals(ajustar_gastos(self.original, 1).to_dict(), self.original.to_dict())
        
        
  def test_ajustar_gastos_com_2_retorna_um_dataframe_com_todos_os_gastos_duplicados(self):
    self.assertEquals(
      ajustar_gastos(self.original, 2)[[
        "tours_expenses", 
        "feed_expenses", 
        "transport_expenses", 
        "shopping_expenses", 
        "other_expenses"]].to_dict("records"), 
      [{
        'tours_expenses': 10.0,
        'feed_expenses': 0.0,
        'transport_expenses': 20.0,
        'shopping_expenses': 6.0,
        'other_expenses': 4.0
      }], "debería haber duplicado tours_expenses, feed_expenses, transport_expenses, shopping_expenses, other_expenses")


  def test_ajustar_gastos_não_muda_as_colunas_que_não_tem_gastos(self):
    self.assertEquals(
      ajustar_gastos(self.original, 2)[[
        "date_id", 
        "total_people", 
        "visits_amount"
      ]].to_dict("records"), 
      [{
        'date_id': 14646,
        'total_people': 2,
        'visits_amount': 2
      }], "debería haber duplicado tours_expenses, feed_expenses, transport_expenses, shopping_expenses, other_expenses")
                                