
<svelte:head>
	<title>회원가입</title>
	<meta name="description" content="Join member | Jobees" />
</svelte:head>

<LayoutGrid>
  <form method="POST" on:submit|preventDefault="{handleRegister}">
  <Cell span={12}>
    <div class="demo-cell">
      <Textfield bind:value={email} type="email" required on:keydown={handleCheckVal} on:keyup={handleCheckVal}>
        <svelte:fragment slot="label">
          <CommonIcon
            class="material-icons"
            style="font-size: 1em; line-height: normal; vertical-align: top;"
            >email</CommonIcon
          > 이메일
        </svelte:fragment>
      </Textfield>
    </div>
  </Cell>
  <Cell span={12}>
    <div class="demo-cell">
      <Textfield bind:value={nickname} label="닉네임" required on:keydown={handleCheckVal} on:keyup={handleCheckVal} />
    </div>
  </Cell>
  <Cell span={12}>
    <div class="demo-cell">
      {#if showButton }
      <Button color="secondary" variant="raised">
        <Label>회원가입</Label>
      </Button>
      {:else}
      <Button color="secondary" disabled>
        <Label>회원가입</Label>
      </Button>
      {/if}      
    </div>
  </Cell>
  </form>
</LayoutGrid>


<script lang="ts">
  import { Icon as CommonIcon } from '@smui/common'
  import LayoutGrid, { Cell } from '@smui/layout-grid'
  import Textfield from '@smui/textfield'
  import Button, { Label } from '@smui/button'

  let nickname:string = ''
  let email:string = ''
  let showButton:boolean = false
  
  function handleCheckVal() {
    if (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) && nickname) {
      showButton = true
    } else {
      showButton = false
    }
    console.log(nickname, email)
  }

  async function handleRegister() {
    const response = await fetch('register.php', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ name, email, password })
    });

    const data = await response.json();

    console.log(data.message);
  }

  // fetch("http://127.0.0.1:8000/hello").then((response) => {
  //   response.json().then((json) => {
  //     message = json.message;
  //   });
  // });
</script>

<style>
  .demo-cell {
    height: 60px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>