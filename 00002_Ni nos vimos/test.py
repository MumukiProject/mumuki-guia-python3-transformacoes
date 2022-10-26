class Test(unittest.TestCase):
  def test_se_elimino_obs(self):
    self.assertFalse("obs" in cines, "se debería haber eliminado la columna obs")
  
  def test_se_elimino_category(self):
    self.assertFalse("category" in cines, "se debería haber eliminado la columna category")    
    
  def test_se_elimino_update_year(self):
    self.assertFalse("update_year" in cines, "se debería haber eliminado la columna update_year")