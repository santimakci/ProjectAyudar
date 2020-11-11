
  jQuery('[name="form1"]').on("submit", selectAll);

  function selectAll() {
    jQuery('[name="roles[]"] option').prop('selected', true).val()
  }

  $(function () {
    $('#add').click(function () {
      let $options = $('#select1 option:selected');
      $options.appendTo("#select2");
    });
    $('#add_all').click(function () {
      let $options = $('#select1 option');
      $options.appendTo("#select2");
    });
    $('#select1').dblclick(function () {
      let $option = $('option:selected', this);
      $option.appendTo('#select2');
    });
    $("#remove").click(function () {
      let $options = $('#select2 option:selected');
      $options.appendTo("#select1");
    });
    $("#remove_all").click(function () {
      let $options = $('#select2 option');
      $options.appendTo('#select1');
    });
    $('#select2').dblclick(function () {
      let $option = $('option:selected');
      $option.appendTo("#select1");
    });
  });
