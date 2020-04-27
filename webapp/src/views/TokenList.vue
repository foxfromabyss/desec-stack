<script>
import CrudList from './CrudList';
import store from '../store';

export default {
  name: 'CrudTokenList',
  extends: CrudList,
  data() {
    const self = this;
    return {
        createable: true,
        updateable: false,
        destroyable: true,
        headlines: {
          table: 'Tokens',
          create: 'Generate New Token',
          destroy: 'Delete Token',
        },
        texts: {
          banner: () => ('Any API Token can be used to perform any DNS operation on any domain in this account. Token scoping is on our roadmap.'),
          create: () => ('Names are purely for your own convenience and carry no technical meaning.'),
          destroy: d => (d.name ? `Delete token with name "${d.name}" and ID ${d.id}?` : `Delete unnamed token with ID ${d.id}?`),
          destroyInfo: () => ('This operation is permanent. Any devices using this token will no longer be able to authenticate.'),
          destroyWarning: d => (d.id == store.state.token.id ? 'This is your current session token. Deleting it will invalidate the session.' : ''),
        },
        columns: {
          id: {
            text: 'ID',
            align: 'left',
            value: 'id',
            readonly: true,
            datatype: 'GenericText',
            searchable: true,
          },
          name: {
            text: 'Name',
            textCreate: 'Token name',
            align: 'left',
            sortable: true,
            value: 'name',
            readonly: false,
            writeOnCreate: true,
            datatype: 'GenericText',
            searchable: true,
          },
          created: {
            text: 'Created',
            align: 'left',
            sortable: true,
            value: 'created',
            readonly: true,
            datatype: 'TimeAgo',
            searchable: false,
          },
          last_used: {
            text: 'Last used',
            align: 'left',
            sortable: true,
            value: 'last_used',
            readonly: true,
            datatype: 'TimeAgo',
            searchable: false,
          },
        },
        actions: [
          {
            key: 'save',
            go: item => self.save(item),
            icon: 'mdi-content-save-edit',
          },
        ],
        paths: {
          list: 'auth/tokens/',
          create: 'auth/tokens/',
          delete: 'auth/tokens/:{id}/',
          update: 'auth/tokens/:{id}/',
        },
        defaultObject: { name: '' },
        postcreate(d) { this.snackbarInfoText = `Your new token is: <code>${d.token}</code><br />It is only displayed once.`; },
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
