# Wiki沙箱

::: {#content dir="ltr" lang="zh-tw"}
你可以在這裡盡情嘗試 wiki 的各項功能, 但是別把四個減號上面的說明改掉了\...(就是本段!) 還有, 請 **\*不要\*** 只是因為想試試看, 就新增沒有內容/意義的頁面.

**提示:** 按住 Shift 鍵再點選 \"[HelpOnEditing](HelpOnEditing)\" 就可以在另一個視窗裡打開編輯說明. IE 用戶請在 \"[HelpOnEditing](HelpOnEditing)\" 上點右鍵, 選「在新視窗開啟」. Firefox 或 Mozilla 用戶可以試試用滑鼠中鍵, 在新的分頁中開啟.

------------------------------------------------------------------------

## 文字格式 {#A.2BZYdbV2g8Xw8-}

*斜體* **粗體** `非調和字`

`倒單引號帶出的非調和字`{.backtick} (這個功能可能會關掉)

放大 [縮小]{.small}

    預先排好格式的段落

    def syntax(highlight):
        print "on"
        return None

## 連結 {#A.2BkCN9UA-}

[HelpOnEditing](HelpOnEditing) [InterWiki](http://moinmoin.wikiwikiweb.de/InterWiki "MoinMoin"){.interwiki} [中文的MoinMoin](./(e4b8ade69687e79a84)MoinMoin.html){.nonexistent}

[http://purl.net/wiki/moin/](http://purl.net/wiki/moin/){.http} [Python](http://www.python.org/){.http}

[someone@the.inter.net](mailto:someone@the.inter.net){.mailto}

### 圖片連結 {#A.2BVxZyR5AjfVA-}

![](http://c2.com/sig/wiki.gif "http://c2.com/sig/wiki.gif"){.external_image}

## 清單 {#A.2BbgVVrg-}

### 圓點 {#A.2BVxOe3g-}

- 第一點
  1.  帶編號的巢狀清單
  2.  編號會一直往上加
- 第二點
- 第三點
  - 又見面了!

  縮排
  - 再縮排

### 辭彙 {#A.2Bj61fWQ-}

專有名詞
:   定義

### 畫圖 {#A.2BdWtXFg-}

[![\[ATTACH\]](/wiki/modernized/img/attach.png "[ATTACH]"){height="32" width="32"}]( "Create new drawing "mytest.tdraw (opens in new window)""){.nonexistent}

# 標題 1 {#A.2BahmYTA_1}

## 標題 2 {#A.2BahmYTA_2}

### 標題 3 {#A.2BahmYTA_3}

#### 標題 4 {#A.2BahmYTA_4}

##### 特別的大小 {#A.2BcnlSJXaEWSdcDw-}

[ПростоТест](./(d09fd180d0bed181d182d0bed0a2d0b5d181d182).html){.nonexistent}

# IRC 對話記錄測試 {#IRC_.2BXA2KcYoYkwRuLIpm-}

    (23:18) <     jroes> ah
    (23:19) <     jroes> hm, i like the way {{{ works, but i was hoping the lines would wrap
    (23:21) -!- gpciceri [~gpciceri@host181-130.pool8248.interbusiness.it] has quit [Read error: 110 (Connection timed out)]
    (23:36) < ThomasWal> you could also write a parser or processor
    (23:38) <     jroes> i could?
    (23:38) <     jroes> would that require modification on the moin end though?
    (23:38) <     jroes> i cant change the wiki myself :x
    (23:39) < ThomasWal> parsers and processors are plugable
    (23:39) < ThomasWal> so you dont need to change the core code
    (23:40) < ThomasWal> you need to copy it to the wiki data directory though
    (23:40) <     jroes> well, what i meant to say was that i dont have access to the box running the wiki
    (23:40) < ThomasWal> then this is no option awdsd asdasd sa asdasd sad asdadasds adasd asd asd asd asd asd a dadad ad adad ad asd asd adad asdasd asd adad as d
    (23:40) <     jroes> yeah :/

[![\[ATTACH\]](/wiki/modernized/img/attach.png "[ATTACH]"){height="32" width="32"}]( "Create new drawing "mytest2.tdraw (opens in new window)""){.nonexistent}

Spanning rows and columns::

- ::: {}
  +:----------:+------------------------------------------------------------------------------------------------------------------:+
  | 2 rows     | row 1                                                                                                             |
  |            +-------------------------------------------------------------------------------------------------------------------+
  |            | row 2 hh hfdsh hfsh jhsdkfh shf jhkvjh xh vjcxh vhcxxvcfdgfdhkh hkhf skjhkjdhfkhdkf hdhkf kjfk jdhskfh df dfhs fs |
  +------------+-------------------------------------------------------------------------------------------------------------------+
  | row 3 over 2 columns                                                                                                           |
  +--------------------------------------------------------------------------------------------------------------------------------+
  :::
:::
