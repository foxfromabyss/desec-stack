<template>
  <v-text-field
    :label="label"
    :disabled="readonly"
    :value="value"
    :type="type || ''"
    placeholder="(optional)"
    @input="input($event)"
    @keyup="keyup($event)"
  />
</template>

<script>
export default {
  name: 'GenericText',
  props: {
    label: {
      type: String,
      required: false,
    },
    readonly: {
      type: Boolean,
      required: false,
    },
    value: {
      type: [String, Number],
      required: true,
    },
    type: {
      type: String,
      required: false,
    },
  },
  methods: {
    input(event) {
      this.$emit('input', event);
    },
    keyup(event) {
      this.$emit('keyup', event);
    },
  },
};
</script>
