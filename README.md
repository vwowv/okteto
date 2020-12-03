# Okteto

okteto开发记录,本项目秉持能用原则。优化什么的忽略



okteto定时修改yml文件以保持应用不休眠。



## 听过github action不开发，计划任务也会停止。

可以使用peaceiris/actions-gh-pages试试。每次运行push到main



```yaml
      # 部署到 GitHub Pages
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          personal_token: ${{ secrets.ACCESS_TOKEN }}
          publish_dir: .
          keep_files: true
          publish_branch: main
          #destination_dir: test
          enable_jekyll: false
          exclude_assets: ''
```

