<template>
  <v-container>
    <v-row>
      <Card title="Encontrá tu centro de donación más cercano" description="Sacá turno y respetando los protocolos, acercá las donaciones." img="map.png" link="/centros" name="Ver centros"/>
      <Card title="Cargá un nuevo centro de donación"  description="¡Si conoces de un centro, no dudes en agregarlo!" img="addCenter.jpg" link="/cargarCentro" name="Añadir centro"/>
      <Card title="Mirá las estadísticas" description="Chequea las estadísticas sobre los centros de ayuda, y como variaron con la pandemia." img="statistics.jpg" link="/estadisticas" name="Ver estadísticas"/>
    </v-row>
  </v-container>
</template>

<script>
import Card from "./Card";
export default {
  name: "Home",
  components: {
    Card
  },
};
</script>
