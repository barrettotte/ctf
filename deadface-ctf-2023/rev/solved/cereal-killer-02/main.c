

int main(void)

{
  int iVar1;
  undefined4 uVar2;
  int in_GS_OFFSET;
  char local_2014 [4096];
  char local_1014 [4096];
  int local_14;
  undefined *local_10;
  
  local_10 = &stack0x00000004;
  local_14 = *(int *)(in_GS_OFFSET + 0x14);
  puts("Luciafer also loves Halloween, so she, too, LOVES SPOOKY CEREALS!");
  puts("She has different favorite villain from 70-80\'s horror movies.");
  printf("What is Luciafer\'s favorite breakfast cereal? ");
  fgets(local_2014,0xfff,stdin);
  decode_str(local_2014,0x3f,&DAT_00012094,local_1014);
  iVar1 = strncmp(local_1014,"CORRECT!!!!!",0xc);


  if (iVar1 == 0) {
    puts(local_1014);
  }
  else {
    printf("%s",
           "INCORRECT....: I\'m afraid that is not Lucia\'s current favorite monster cereal.  She is  kind of capricious, you know, so it changes often.\n"
          );
  }
  uVar2 = 0;
  if (local_14 != *(int *)(in_GS_OFFSET + 0x14)) {
    uVar2 = __stack_chk_fail_local();
  }
  return uVar2;
}

void decode_str(int param_1,int param_2,int param_3,int param_4)

{
  int local_10;
  int local_c;

  // decode_str(local_2014,0x3f,&DAT_00012094,local_1014);
  //            *input, 4096, static data?, *flag
  
  local_10 = 0;
  local_c = 0;
  while (local_c < param_2) {
    *(byte *)(param_4 + local_c) = *(byte *)(param_3 + local_c) ^ *(byte *)(param_1 + local_10);
    local_c = local_c + 1;
    local_10 = local_10 + 1;
    if (0xb < local_10) { // 11
      local_10 = 0;
    }
  }
  *(undefined *)(param_4 + local_c) = 0;
  return;
}
