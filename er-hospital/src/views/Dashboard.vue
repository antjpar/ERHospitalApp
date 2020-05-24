<template>
  <div :class="$style.dashThings">
    <label :class="$style.graph">
      Vor Ort:
      <v-progress-circular width="20" size="150" value="10" color="brown">
        2
      </v-progress-circular>
    </label>
    <label :class="$style.graph">
      Unterwegs:
      <v-progress-circular width="20" size="150" value="10" color="blue">
        10
      </v-progress-circular>
    </label>
    <label :class="$style.graph">
      Noch zu Hause:
      <v-progress-circular width="20" size="150" value="55" color="orange">
        55
      </v-progress-circular>
    </label>
    <label :class="$style.graph">
      Durchschnittliche Wartezeit:
      <v-progress-circular width="20" size="150" value="60" color="green">
        1h 30m
      </v-progress-circular>
    </label>
  </div>
</template>

<script>
export default {
  name: 'Dashboard',
}
</script>

<style module lang="scss">
.graph {
  text-align: center;
  display: grid;
  column-gap: 1rem;
  row-gap: 2rem;
  max-width: 15vw;
  grid-template-rows: 1fr 6fr;
  word-break: break-word;
}
.dashThings {
  display: flex;
  flex-wrap: wrap;
  padding: 5rem;
  gap: 10vw;
  justify-content: center;
}
</style>
