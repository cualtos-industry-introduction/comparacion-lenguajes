public class Inventario {

  class Objeto {

    String nombre = "";
    int cantidad = 0;

    public Objeto(String nombre) {
      this.nombre = nombre;
    }

    public Boolean actualizarCantidad(int nuevaCantidad) {
      this.cantidad += nuevaCantidad;
    }
  }

  public static void main(String args[]) {
    Objeto botellaDeAgua = new Objeto("Botella de agua");
    botellaDeAgua.actualizarCantidad(10);
    System.out.println(botellaDeAgua.nombre);
  }
}
