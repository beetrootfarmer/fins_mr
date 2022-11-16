import Vue from 'vue'

// font awesome 사용 라이브러리, 컴포넌트 추가
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

// 설치했던 아이콘파일에서 해당 아이콘만 불러옵니다. 
import { faHouse,faLink, faRedo, faUndo } from "@fortawesome/free-solid-svg-icons";
import { faTrashAlt } from "@fortawesome/free-regular-svg-icons";

// 불러온 아이콘을 라이브러리에 담습니다. 
library.add(faTrashAlt);
library.add(faHouse,faLink, faRedo, faUndo); // 필요한 아이콘을 가져오는 부분

// fontawesome아이콘을 Vue탬플릿에 사용할 수 있게 등록해 줍니다. 
Vue.component('font-awesome-icon', FontAwesomeIcon)