<template>
  <div>
    <ChartPie/>
    <ChartBar/>
  </div>
</template>


<script>
import ChartPie from "./ChartPie"
import ChartBar from "./ChartBar"

export default {
  components: {
    ChartPie,
    ChartBar
  },
  data: () => ({}),
};
</script>
