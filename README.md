# abcDict

## example

```yaml
# test.yaml
path: ${ALLUSERSPROFILE}

info:
  none1: ''
  none2: None
  name: ${name}
  name_default: ${name|default:msbrm}
  age: ${age}
  age_default: ${age|default:18}
  age_default_int: ${age|default:18|type:int}

info_str: 我是name:${name},name_default:${name|default:$<name>},今年刚满age:${age},age_default:${age|default:18}岁
info_str2: ${HOME}xxxxxxx${age|default:18|type:int}xxxxxxx${HOME}
file_path: /home/${FILE|default:abc}/abc.test
```
