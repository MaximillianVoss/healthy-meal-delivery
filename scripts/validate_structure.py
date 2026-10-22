from pathlib import Path
import sys
root=Path(__file__).resolve().parents[1]
required=['README.md','.gitignore','.env.example','.github/ISSUE_TEMPLATE/bug_report.yml','.github/PULL_REQUEST_TEMPLATE.md','.github/workflows/repository-checks.yml','docs/BRANCH_PROTECTION.md','docs/ARCHITECTURE.md','src/README.md','tests/README.md','deploy/README.md']
errors=[f'Нет файла {p}'for p in required if not(root/p).is_file()]
for p in ['README.md','docs/ARCHITECTURE.md','docs/BRANCH_PROTECTION.md']:
 if(root/p).is_file()and len((root/p).read_text('utf-8').strip())<100:errors.append(f'Пустое описание {p}')
for line in(root/'.env.example').read_text('utf-8').splitlines():
 if line.startswith('DB_PASSWORD=')and line!='DB_PASSWORD=':errors.append('Пароль в примере должен оставаться пустым')
if(root/'.env').exists():errors.append('.env не входит в публикуемую структуру')
if errors:print('\n'.join(errors));sys.exit(1)
print(f'PASS: {len(required)} обязательных файлов, безопасный пример окружения и документация')
