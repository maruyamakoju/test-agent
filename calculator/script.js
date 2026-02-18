(function () {
  'use strict';

  const $ = (id) => document.getElementById(id);
  const display = $('current');
  const expr = $('expression');

  let current = '0';
  let previous = '';
  let operator = '';
  let resetNext = false;

  const OPERATOR_SYMBOLS = { '+': '+', '-': '\u2212', '*': '\u00d7', '/': '\u00f7' };

  function updateDisplay() {
    display.textContent = current;
    expr.textContent = previous && operator
      ? previous + ' ' + OPERATOR_SYMBOLS[operator]
      : '';
  }

  function calculate(a, op, b) {
    const x = parseFloat(a);
    const y = parseFloat(b);
    switch (op) {
      case '+': return x + y;
      case '-': return x - y;
      case '*': return x * y;
      case '/': return y === 0 ? 'Error' : x / y;
      default: return y;
    }
  }

  function formatNumber(n) {
    if (typeof n === 'string') return n;
    if (!isFinite(n)) return 'Error';
    // Avoid floating-point display artifacts
    const str = parseFloat(n.toPrecision(12)).toString();
    return str.length > 14 ? parseFloat(n).toExponential(6) : str;
  }

  function inputNumber(digit) {
    if (resetNext) {
      current = digit;
      resetNext = false;
    } else {
      current = current === '0' ? digit : current + digit;
    }
    updateDisplay();
  }

  function inputDecimal() {
    if (resetNext) {
      current = '0.';
      resetNext = false;
    } else if (!current.includes('.')) {
      current += '.';
    }
    updateDisplay();
  }

  function inputOperator(op) {
    if (operator && !resetNext) {
      const result = calculate(previous, operator, current);
      current = formatNumber(result);
      previous = current;
    } else {
      previous = current;
    }
    operator = op;
    resetNext = true;
    updateDisplay();
  }

  function inputEquals() {
    if (!operator) return;
    const result = calculate(previous, operator, current);
    expr.textContent = previous + ' ' + OPERATOR_SYMBOLS[operator] + ' ' + current + ' =';
    current = formatNumber(result);
    display.textContent = current;
    previous = '';
    operator = '';
    resetNext = true;
  }

  function inputClear() {
    current = '0';
    previous = '';
    operator = '';
    resetNext = false;
    updateDisplay();
  }

  function inputBackspace() {
    if (resetNext) return;
    current = current.length > 1 ? current.slice(0, -1) : '0';
    updateDisplay();
  }

  function inputPercent() {
    current = formatNumber(parseFloat(current) / 100);
    updateDisplay();
  }

  function inputToggleSign() {
    if (current === '0') return;
    current = current.startsWith('-') ? current.slice(1) : '-' + current;
    updateDisplay();
  }

  // Button click handler
  document.querySelector('.buttons').addEventListener('click', function (e) {
    const btn = e.target.closest('.btn');
    if (!btn) return;
    const action = btn.dataset.action;
    const value = btn.dataset.value;

    switch (action) {
      case 'number':     inputNumber(value); break;
      case 'decimal':    inputDecimal(); break;
      case 'operator':   inputOperator(value); break;
      case 'equals':     inputEquals(); break;
      case 'clear':      inputClear(); break;
      case 'backspace':  inputBackspace(); break;
      case 'percent':    inputPercent(); break;
      case 'toggle-sign': inputToggleSign(); break;
    }
  });

  // Keyboard support
  document.addEventListener('keydown', function (e) {
    if (e.key >= '0' && e.key <= '9') { inputNumber(e.key); return; }
    switch (e.key) {
      case '.':         inputDecimal(); break;
      case '+':         inputOperator('+'); break;
      case '-':         inputOperator('-'); break;
      case '*':         inputOperator('*'); break;
      case '/':         e.preventDefault(); inputOperator('/'); break;
      case 'Enter':
      case '=':         inputEquals(); break;
      case 'Backspace': inputBackspace(); break;
      case 'Escape':    inputClear(); break;
      case '%':         inputPercent(); break;
    }
  });

  updateDisplay();
})();
