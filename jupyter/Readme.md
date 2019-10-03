
# Jupyter notebook 

## Install

### jupyter notebook

- `pip install jupyter`

### jupyter qtconsole

- jupyter [qtconsole](http://blog.naver.com/PostView.nhn?blogId=msyang59&logNo=220568393312)을 쓰고 싶으면
  pyqt 필요 (현재 필자는 pyqt5) or qtconsole을 직접 install
</br>
- ```pip install jupyter```
- ```pip install pyqt qtconsole```

### Theme

- #### 설치 

    - `pip install jupyterthemes`

- #### 테마 리스트 보기

    - `jt -l` : 입력하면 현재 가능한 테마 리스트가 나온다

    * Available Themes:
        chesterish
        grade3
        gruvboxd
        gruvboxl
        monokai
        oceans16
        onedork
        solarizedd
        solarizedl

- #### 테마 적용

    - `jt -t theme-name`

    - 적용 후 실행한 jupyter에서 바꿔가며 고르기 
</br>
    - `Dark한 거 좋아하면 chesterish 추천`
    - `jt -t chesterish`

### Setting on jupyter notebook

- #### 설정 파일 생성하기
    - ```jupyter notebook --generate-config``` : 주피터 노트북 셋팅 파일 생성
    - 주로 Home dir 위치에 생성된다. (```~/.jupyter/jupyter_noteboook_config.py```)

</br>

- #### Customizing
    - ```~/.jupyter/``` 아래에 ```custom```이라는 폴더 생성, ```custom.css```라는 파일을 만든다.
    - 만든 ```custom.css``` 파일을 수정하여 설정을 적용한다.

    - Example
        - Font : consolas
        - Font-size : 12pt
        
        ```
        .CodeMirror pre {font-family: Consolas; font-size: 12pt; line-height: 140%;}
        .container { width:100% !important; }
        div.output pre{
            font-family: Consolas;
            font-size: 12pt;
        }
        ```