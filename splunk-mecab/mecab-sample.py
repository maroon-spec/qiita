# -*- coding: utf-8 -*-
import sys
import MeCab

m = MeCab.Tagger("-Owakati")
print m.parse("こんにちは皆さん。今日はいい天気ですね")
