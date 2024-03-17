# [1.4.0](https://github.com/strukovsv/PAQLang/compare/v1.3.0...v1.4.0) (2024-03-17)


### docs

* подправил атрибуты для oracle ([222d3b5](https://github.com/strukovsv/PAQLang/commit/222d3b5e4ec5d7f13206dd067db8d3371a671f2a))
* ссылки на тесты d github ([5840080](https://github.com/strukovsv/PAQLang/commit/58400803ebcacbe267df815ac62aaee011daf424))

### feat

* добавил github в oracle и вынес получение запроса в отдельную процедуру ([80944e2](https://github.com/strukovsv/PAQLang/commit/80944e22b27dcca2e67a08fc520c7468b2378831))
* сделал отдельную функцию получение данных из файла и git ([762be9f](https://github.com/strukovsv/PAQLang/commit/762be9f098568288fa3dc88e557ed4ead908e5b6))

# [1.3.0](https://github.com/strukovsv/PAQLang/compare/v1.2.2...v1.3.0) (2024-03-16)


### chore

* ошибка стиля flake8 ([4480b82](https://github.com/strukovsv/PAQLang/commit/4480b82817eed120f9b7e057a76a17e4f810fe86))

### ci

* action  последовательное выполнение ([0d1b265](https://github.com/strukovsv/PAQLang/commit/0d1b2657c3cab6fa49e80772bd7bdee9d046fec0))
* line actions ([30a5904](https://github.com/strukovsv/PAQLang/commit/30a5904af42020f4bce99a5590d437033a2f4349))
* test error ([18c5956](https://github.com/strukovsv/PAQLang/commit/18c5956c87fc96ec8fb26f37bc4aa697cc912d56))
* test failure ([367c88a](https://github.com/strukovsv/PAQLang/commit/367c88a8e92ad3377a298618937f3b81c92df93b))
* test failure ([8524513](https://github.com/strukovsv/PAQLang/commit/8524513c65cfc874d26169e3333b8fefa0d4a240))
* test success ([bda12ff](https://github.com/strukovsv/PAQLang/commit/bda12ff74f334b5323d66630222a460a317e34a9))
* test success ([a6f18d4](https://github.com/strukovsv/PAQLang/commit/a6f18d482448b818d93b463dd4e3d523f5418547))
* Update .releaserc.json ([5842ffa](https://github.com/strukovsv/PAQLang/commit/5842ffa7e252e90860c38529d0a25b41f9cda6df))
* Update lint-flake8.yml ([1c00fe2](https://github.com/strukovsv/PAQLang/commit/1c00fe23453bbf364575ed774d0bbc08b98e8755))
* Update pytest.yml ([4ef28e8](https://github.com/strukovsv/PAQLang/commit/4ef28e8ebc6e21272461370a9922a5b54da32b51))
* Update release.yml ([a015b11](https://github.com/strukovsv/PAQLang/commit/a015b114a1e570a29b0dd4ac0780cfd4adeb6da2))
* Update release.yml ([ba20996](https://github.com/strukovsv/PAQLang/commit/ba209966c6746ccd301afe57b986a7538e601d8a))
* Update release.yml ([de5699f](https://github.com/strukovsv/PAQLang/commit/de5699febede1c260ee81cd9d9a9b809d16aaa0f))
* вернул steps ([9da4334](https://github.com/strukovsv/PAQLang/commit/9da4334c67bb77054932c33cd4e67199454c0706))
* параллельное выполнение тестов и проверок перед build ([06c9d8c](https://github.com/strukovsv/PAQLang/commit/06c9d8c614c47d0027614f050c819152921379e0))
* поменял name в actions ([cea2234](https://github.com/strukovsv/PAQLang/commit/cea2234610ac641960acdca5ff1c1627a2d407b9))
* релиз пока оставим только от PyTest. lint не останавливает релиз ([c517e70](https://github.com/strukovsv/PAQLang/commit/c517e70e2c53ca47050fac33b61b358db8eae87a))
* сделал test ошибочным для проверки ([4894198](https://github.com/strukovsv/PAQLang/commit/4894198a2b87a2033c807dd3de892d1fd6ba4540))
* убрал steps ([0a5bc51](https://github.com/strukovsv/PAQLang/commit/0a5bc511720767427b150de432beb521688e46e5))

### docs

* Update README.md ([b22cefd](https://github.com/strukovsv/PAQLang/commit/b22cefdeebef7a5006d794941affe80dd7edadb2))
* добавить наименование процедуры в оглавление ([7ea3eba](https://github.com/strukovsv/PAQLang/commit/7ea3eba2215704ab5b74309c47b9a61631ac2a29))
* значительно подправил документацию по функциям ([11aba3a](https://github.com/strukovsv/PAQLang/commit/11aba3a8b9ec66f505a8bbea64a2db20e616ed24))
* ошибки ссылок в топике еще подправил ([0ce3590](https://github.com/strukovsv/PAQLang/commit/0ce3590ed49f1d6f11b9ddf9133988d5add309fd))
* подправил ссылки из оглавления на функции ([5e45eba](https://github.com/strukovsv/PAQLang/commit/5e45eba7ba1a56441cba04164944320f61df6e9d))
* разбил функции по группам ([8d06e85](https://github.com/strukovsv/PAQLang/commit/8d06e85a665ab280aec761563c2324c3499d917a))

### feat

* api github projects ([d5af577](https://github.com/strukovsv/PAQLang/commit/d5af577e6cc3720b9c80866ba9bc53f35500e736))
* github branches ([85372d4](https://github.com/strukovsv/PAQLang/commit/85372d4a97ece0e74c3d9faa0b1174483d5e43aa))
* работа с api github тесты и документация ([32f74fd](https://github.com/strukovsv/PAQLang/commit/32f74fd4d8118cd0cb54cd9e9f50f02eea022e1b))

### fix

* ошибка работы с ISO форматом даты в атрибуте since api gitlab ([2175a00](https://github.com/strukovsv/PAQLang/commit/2175a0097c324a2394e5c1f6d62e3fcf1b1e7f54))

### test

* bugfix test_distinct ([3be0c91](https://github.com/strukovsv/PAQLang/commit/3be0c9132cd0455e5b71b5ba349bb31856e5fed4))

## [1.2.2](https://github.com/strukovsv/PAQLang/compare/v1.2.1...v1.2.2) (2024-03-13)


### ci

* pytest -> lint -> release ([de80272](https://github.com/strukovsv/PAQLang/commit/de802726c347a0ace32fd3b51c4a9e5d0b71377e))
* Update lint-flake8.yml ([2375a39](https://github.com/strukovsv/PAQLang/commit/2375a39811e07079c1addb80b0a828ec5e50b75d))
* Update release.yml ([387de03](https://github.com/strukovsv/PAQLang/commit/387de03ada0e2f3ae06def78f07766b9b6b93ccb))
* Update release.yml ([f782823](https://github.com/strukovsv/PAQLang/commit/f782823c0e5d722741d86e97fb159c29b228d745))
* Update release.yml ([d58a276](https://github.com/strukovsv/PAQLang/commit/d58a276f549132553d9ae63e485639253cd5452c))
* Update release.yml ([ba18549](https://github.com/strukovsv/PAQLang/commit/ba185497f28fb8ad867f47c74b5b5007e65cfed8))
* Update release.yml ([c913ec7](https://github.com/strukovsv/PAQLang/commit/c913ec714fc3fb49e9bf74ba7f07db43107eb3fd))
* отдельно все задания. release проверяет успешность других заданий ([1fcb9cc](https://github.com/strukovsv/PAQLang/commit/1fcb9cc33c2acdf1af6c811074ffde6c9d273bd0))
* проверка выката ошибки новой версии ([10608d4](https://github.com/strukovsv/PAQLang/commit/10608d4976d14e8343397f05abc2de729893dcfa))

### docs

* Update README.md ([fdcd763](https://github.com/strukovsv/PAQLang/commit/fdcd76349d55d929a596ff112c6fb37440bf21d9))

### style

* Update _version.py ([9bef5c6](https://github.com/strukovsv/PAQLang/commit/9bef5c63314eb1d994ae4f594a551450cf5d47fd))

## [1.2.1](https://github.com/strukovsv/PAQLang/compare/v1.2.0...v1.2.1) (2024-03-13)


### chore

* exclude CHANGELOG.md ([840c8af](https://github.com/strukovsv/PAQLang/commit/840c8af5526ca8f822e55c9b53e4b706537dde0e))
* ignore changelog.md ([fd427be](https://github.com/strukovsv/PAQLang/commit/fd427befa26496fe0acaaf682bcb10e9fc542ae3))
* markdown файлы подправил ([0758820](https://github.com/strukovsv/PAQLang/commit/0758820399a3d827b9616396c2a61dfe1c71a8da))
* двойные кавычки !!! ([73a825b](https://github.com/strukovsv/PAQLang/commit/73a825b9700e6ac53fb0cf1e98a8f30710dac6ba))
* исправлены ошибке в правописании ([69b4929](https://github.com/strukovsv/PAQLang/commit/69b492954b0e6a3630cc78be24a91b882c46da86))

### ci

* init lint flake8 ([0cbae1c](https://github.com/strukovsv/PAQLang/commit/0cbae1cd3e823e21b29591c623766a64ef6f6dfc))
* Update lint-flake8.yml ([8fee2c7](https://github.com/strukovsv/PAQLang/commit/8fee2c76399c065878594e2bcdcdda7dd2322d02))
* Update lint-flake8.yml ([3838f7c](https://github.com/strukovsv/PAQLang/commit/3838f7cf84caa16e38711e6f1cea48894da0d825))

### docs

* простой пример программмы ([0b6e0a0](https://github.com/strukovsv/PAQLang/commit/0b6e0a081bd0af907917f4ea057e70e592f2e02d))

### style

* flake python stage 2 ([c280458](https://github.com/strukovsv/PAQLang/commit/c28045874895170277adae0e870541d31ba8b084))
* python flake8 stage 1 ([2214fd1](https://github.com/strukovsv/PAQLang/commit/2214fd1ff5fa536bca01dfdae961481c299ec1a2))
* Update _version.py ([839921c](https://github.com/strukovsv/PAQLang/commit/839921ce8e569527afd095e6518d8c69bfb000e0))
* Update _version.py ([3d68a9a](https://github.com/strukovsv/PAQLang/commit/3d68a9a47873780351a82894f7ed4b404f229f0e))
* поправил test_call ([1f2fdf8](https://github.com/strukovsv/PAQLang/commit/1f2fdf8b9657d426db74065d508c29d47112b38a))

# [1.2.0](https://github.com/strukovsv/PAQLang/compare/v1.1.0...v1.2.0) (2024-03-11)


### feat

* если передан код программы как текст, то преобразовать в объект из JSON или YAML ([b043c43](https://github.com/strukovsv/PAQLang/commit/b043c43ef28aa825c81e4cfc51f5cb25be85087a))

# [1.1.0](https://github.com/strukovsv/PAQLang/compare/v1.0.5...v1.1.0) (2024-03-11)


### chore

* убрал отладочную информацию ([30df899](https://github.com/strukovsv/PAQLang/commit/30df899c6ebaf968a5032855a606d32025419b32))

### ci

* pytest path ([f8a0576](https://github.com/strukovsv/PAQLang/commit/f8a057695772d22545dd502ef90642be0aa14b8f))

### feat

* добавил атрибуты to_json и split в функцию freads, поправил вычисление маршрутов файлов ([ad3b585](https://github.com/strukovsv/PAQLang/commit/ad3b585033ec7c237eca5a333daea28f57e1b1c8))

### test

* вывод пути к в лог файлам ([8112466](https://github.com/strukovsv/PAQLang/commit/8112466025db39b04943dd4983ef46a39fbb5cb8))

## [1.0.5](https://github.com/strukovsv/PAQLang/compare/v1.0.4...v1.0.5) (2024-03-11)


### ci

* Create pytest.yml ([cf5d414](https://github.com/strukovsv/PAQLang/commit/cf5d414f96574e7b55ca163edd5074eec583c406))
* Update pytest.yml ([56e68e6](https://github.com/strukovsv/PAQLang/commit/56e68e6dadf0f1406ff63db0a7bce88ba519b932))
* Update pytest.yml ([103cbf7](https://github.com/strukovsv/PAQLang/commit/103cbf7fdb27077e6803962e28f2fa307f05ce93))
* Update pytest.yml ([89f648d](https://github.com/strukovsv/PAQLang/commit/89f648d19077c2e0c177de9d9bec187cd0460c83))
* Update pytest.yml ([78f9333](https://github.com/strukovsv/PAQLang/commit/78f93337b034d93fe45c0a44a236b807bc2b70af))
* Update pytest.yml ([f37946e](https://github.com/strukovsv/PAQLang/commit/f37946eb7e7571818d31525d0bfcb2099968768d))
* Update pytest.yml ([ab0d441](https://github.com/strukovsv/PAQLang/commit/ab0d4413649d548264dd877f8e8dbd1ca1884267))

### docs

* Delete changelog.md ([5f8e434](https://github.com/strukovsv/PAQLang/commit/5f8e434a6f2bb2801188883277da2b8dacec172b))
* readme ([1a3411d](https://github.com/strukovsv/PAQLang/commit/1a3411dcf69da224e179793298b9d5d866ccc45e))
* Update README.md ([adca9ee](https://github.com/strukovsv/PAQLang/commit/adca9ee05c853211dc4367b2c7985c2a3b6fb500))
* Update README.md ([a3c8592](https://github.com/strukovsv/PAQLang/commit/a3c85929925f21547c9e649ab597cc606716d8fe))

### fix

* заменить регистр в имени файла __init__.py ([27ce7de](https://github.com/strukovsv/PAQLang/commit/27ce7de5658ae464ca55226066567454b06d010a))

### test

* отложил тесты с файлами ([29b347b](https://github.com/strukovsv/PAQLang/commit/29b347bc3f86c7718ec282d970d41dbc1fa147a3))
* подправил тесты. Временно исключил временные файлы ([ff8bda1](https://github.com/strukovsv/PAQLang/commit/ff8bda10bdc2388ccf9e48d2a90a3cfb1f322c5a))

## [1.0.4](https://github.com/strukovsv/PAQLang/compare/v1.0.3...v1.0.4) (2024-03-10)


### ci

* Update python-publish.yml ([c3c29de](https://github.com/strukovsv/PAQLang/commit/c3c29de02ea745c12b014507a1277f8921f64d6b))
* Update release.yml ([fb1e35c](https://github.com/strukovsv/PAQLang/commit/fb1e35c722c78a21948079e35479d754f876dca5))

### style

* program.py ([fe15bd6](https://github.com/strukovsv/PAQLang/commit/fe15bd671db589eecf60eb537dd6a12bb36fb3b9))

## [1.0.3](https://github.com/strukovsv/PAQLang/compare/v1.0.2...v1.0.3) (2024-03-10)


### style

* program.py ([6f7dec6](https://github.com/strukovsv/PAQLang/commit/6f7dec6fd63d81c9fb3123d56802e541716ac9c2))

## [1.0.2](https://github.com/strukovsv/PAQLang/compare/v1.0.1...v1.0.2) (2024-03-10)


### style

* param.py ([972e25b](https://github.com/strukovsv/PAQLang/commit/972e25b96b30655a5050e6d37f5aa23eb8834cc7))

## [1.0.1](https://github.com/strukovsv/PAQLang/compare/v1.0.0...v1.0.1) (2024-03-10)


### ci

* Update release.yml ([5d1489f](https://github.com/strukovsv/PAQLang/commit/5d1489f14964a190e814ed853f5ad5502c078152))

### style

* data.py ([32ce6aa](https://github.com/strukovsv/PAQLang/commit/32ce6aa58f4ff95cc987687073389e3b8cc889ab))

# 1.0.0 (2024-03-10)


### ci

* Create lint.yml ([49197ff](https://github.com/strukovsv/PAQLang/commit/49197ff8829110faee6a37f52d0e3fa6072853bb))
* Update lint.yml ([10c9c4e](https://github.com/strukovsv/PAQLang/commit/10c9c4ee68966b263adab1ad326b73ab3482160b))
* Update lint.yml ([ccd79b6](https://github.com/strukovsv/PAQLang/commit/ccd79b6e297c16ce7859069db9a48117f0a90e03))
* Update python-publish.yml ([79d1e43](https://github.com/strukovsv/PAQLang/commit/79d1e43061b9daf067f2d9f08b7c2af2b037cfed))
* Update python-publish.yml ([8616057](https://github.com/strukovsv/PAQLang/commit/861605730ad211c79f4bdf0696cc2d1ffbe84a0b))
* Update python-publish.yml ([c348ddf](https://github.com/strukovsv/PAQLang/commit/c348ddf83dc8e42077c9b247581f9fe80b6b4da3))
* Update README.md ([c3077ef](https://github.com/strukovsv/PAQLang/commit/c3077ef248d864dfab5b0d328cc0dfa9833207cd))
* создание релиза при вливании в мастерскую ветку, в зависимости от типа комментария ([64d7843](https://github.com/strukovsv/PAQLang/commit/64d78434419daf97237523a78093a6e20587dc8e))

### style

* __init_.py ([9d9a469](https://github.com/strukovsv/PAQLang/commit/9d9a46945362e67f4a8f98fba55339a5024bab7f))
