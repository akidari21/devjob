
<svelte:head>
	<title>회원가입</title>
	<meta name="description" content="Join member | Jobees" />
</svelte:head>


<div class="columns margins">
    <div class="margins">
      <Textfield bind:value={valueElementsLabel} type="이메일주소" required>
        <svelte:fragment slot="label">
          <CommonIcon
            class="material-icons"
            style="font-size: 1em; line-height: normal; vertical-align: top;"
            >email</CommonIcon
          > Email
        </svelte:fragment>
      </Textfield>
    </div>
    <div>
      <Textfield bind:value={valueA} label="닉네임" required />
    </div>
    <div class="margins">
      <Button color="secondary" on:click={() => clicked++} variant="raised">
        <Label>회원가입</Label>
      </Button>
    </div>
  </div>


<script lang="ts">
  import Textfield from '@smui/textfield'
  import Button, { Label } from '@smui/button';
  import { Icon as CommonIcon } from '@smui/common'
  
  let clicked = 0;
  let valueA = '';
  let valueB = '';
  let valueC = '';
  let valueElementsLabel = ''
  // let message;

  // fetch("http://127.0.0.1:8000/hello").then((response) => {
  //   response.json().then((json) => {
  //     message = json.message;
  //   });
  // });

  
</script>